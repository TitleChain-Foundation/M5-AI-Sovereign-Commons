// Read-only browser acceptance; no account, credential or tool activation.
const {chromium}=require('playwright');
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),assert=require('node:assert/strict');
const root=path.resolve(process.argv[2]||'_site'),output=path.resolve(process.argv[3]||'browser-evidence');fs.mkdirSync(output,{recursive:true});const server=http.createServer((req,res)=>{let f=path.resolve(root,'.'+decodeURIComponent(req.url.split('?')[0]));if(!f.startsWith(root+path.sep)){res.writeHead(403);return res.end();}if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');if(!fs.existsSync(f)){res.writeHead(404);return res.end();}res.setHeader('Content-Type',f.endsWith('.html')?'text/html':f.endsWith('.js')?'text/javascript':f.endsWith('.json')?'application/json':f.endsWith('.css')?'text/css':'application/octet-stream');res.end(fs.readFileSync(f));});
(async()=>{await new Promise(ok=>server.listen(0,'127.0.0.1',ok));let browser;let rows=[];try{browser=await chromium.launch(process.env.M5_CHROME_PATH?{executablePath:process.env.M5_CHROME_PATH}:{});const base='http://127.0.0.1:'+server.address().port;
for(const width of [1280,390]){
 const page=await browser.newPage({viewport:{width,height:900}}),errors=[],httpErrors=[];page.on('pageerror',e=>errors.push(e.message));page.on('response',r=>{if(r.url().startsWith(base)&&r.status()>=400)httpErrors.push(r.url());});
 await page.goto(base+'/index.html#/search/',{waitUntil:'networkidle'});await page.getByRole('heading',{name:'Search the Commons',exact:true}).waitFor();assert.ok(await page.locator('main h1').evaluate(e=>e.getBoundingClientRect().top<innerHeight),'Search title must appear in the initial viewport, not below an empty main');
 for(const label of ['Type','Pathway','Status']){const opts=await page.getByRole('combobox',{name:label,exact:true}).locator('option').allTextContents();assert.ok(opts.length>1);assert.ok(opts.every(t=>t.trim().length>0),label+' labels');}
 const results=page.locator('[data-screen-label="Search"] ul a');assert.equal(await results.count(),79,'Preserve all existing indexed records');
 const links=await results.evaluateAll(es=>es.map(e=>({text:e.textContent,href:e.getAttribute('href')})));
 assert.equal(links.filter(x=>x.href.startsWith('https://m5labs-8770fb.gitlab.io/#calculators')).length,17);
 assert.ok((await page.locator('body').innerText()).includes('79 results'));assert.equal(await page.locator('a[href*="titlechain-foundation.gitlab.io/m5labs"]').count(),0);
 await page.getByRole('combobox',{name:'Type',exact:true}).selectOption('Project');assert.equal(await results.count(),10);
 await page.getByRole('combobox',{name:'Pathway',exact:true}).selectOption('business-enterprise');assert.ok((await results.count())>0 && (await results.count())<10);
 await page.getByRole('combobox',{name:'Pathway',exact:true}).selectOption('');await page.getByRole('combobox',{name:'Type',exact:true}).selectOption('');
 await page.getByRole('searchbox').fill('no-such-result-xyz');await page.getByRole('searchbox').press('Tab');await page.getByText('No results.',{exact:true}).waitFor();await page.getByRole('searchbox').fill('');await page.getByRole('searchbox').press('Tab');
 // Every local search destination remains a valid existing view; source-only and external results stay distinct.
 for(const link of links.filter(x=>x.href.startsWith('#/'))){await page.evaluate(h=>{location.hash=h},link.href);await page.waitForTimeout(80);assert.equal(await page.getByText('This page is not in the Commons.',{exact:true}).count(),0,link.href);assert.ok(await page.locator('main h1').count()>0,link.href);}
 for(const [slug,file] of [['iwbe','iwbe.html'],['iswe','iwbe.html#iswe'],['m5labs-calculators','labs.html']]){
  await page.goto(base+'/index.html#/projects/'+slug+'/overview/',{waitUntil:'networkidle'});await page.waitForFunction(file=>Array.from(document.querySelectorAll('a[href]')).some(a=>a.getAttribute('href')===file),file);
  const a=page.locator('a[href="'+file+'"]');await a.click();await page.waitForLoadState('networkidle');assert.ok((await page.locator('h1').count())>0,file);
  if(file.includes('#iswe'))assert.equal(await page.locator('#iswe').count(),1);
 }
 await page.goto(base+'/index.html#/search/',{waitUntil:'networkidle'});const fronts=await page.getByRole('navigation',{name:'Explore front ends',exact:true}).locator('a').evaluateAll(es=>es.map(e=>e.href));assert.equal(fronts.length,5);
 for(const href of fronts.filter(h=>new URL(h).origin===base)){const q=await browser.newPage();await q.goto(href,{waitUntil:'networkidle'});assert.ok(await q.locator('h1').count()>0,href);await q.close();}
 assert.deepEqual(errors,[],'runtime errors');assert.deepEqual(httpErrors,[],'local HTTP errors'); await page.screenshot({path:path.join(output,'SEARCH-'+width+'.png'),fullPage:true}); assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'search viewport overflow');
 await page.screenshot({path:path.join(output,'SEARCH-'+width+'.png'),fullPage:true});rows.push({width,searchResults:79,localDestinations:links.filter(x=>x.href.startsWith('#/')).length,status:'PASS',filters:'PASS',designedPages:'PASS'});await page.close();
}
fs.writeFileSync(path.join(output,'BROWSER_RESULTS.json'),JSON.stringify(rows,null,2));console.log(JSON.stringify(rows));
}finally{if(browser)await browser.close();server.close();}})().catch(e=>{console.error(e);fs.writeFileSync(path.join(output,'FAILURE.json'),JSON.stringify({status:'FAIL',error:e.message},null,2));process.exitCode=1;server.close();});
