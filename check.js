// Проверка собранного index.html: запускает движок в Node и открывает каждый шаг каждого курса.
// Запуск: node check.js
const fs = require("fs");
const html = fs.readFileSync(__dirname + "/index.html", "utf8");
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]).join("\n");
const mk = () => ({ style:{}, dataset:{}, classList:{add(){},remove(){}}, appendChild(){}, setAttribute(){}, focus(){}, scrollIntoView(){},
  querySelector(){ return mk(); }, querySelectorAll(){ return []; }, set innerHTML(v){ this._h = v; }, get innerHTML(){ return this._h || ""; } });
global.localStorage = { getItem(){ return null; }, setItem(){} };
global.location = { hash:"", pathname:"/", search:"" }; global.history = { replaceState(){} };
global.window = { innerWidth:1200, scrollTo(){}, addEventListener(){} };
global.document = { title:"", getElementById:()=>mk(), createElement:()=>mk() };
const problems = [];
eval(scripts + `
for (const c of CATALOG) {
  openCourse(c.id);
  for (const s of steps(c)) { cs(c.id).cur = s.id; render(); }
  c.COURSE.forEach(m => {
    if (m.quiz.length !== 3) problems.push(c.id + " " + m.id + ": в тесте модуля не 3 вопроса");
    m.quiz.forEach((q, i) => { if (q.a.length !== 4 || q.c < 0 || q.c > 3) problems.push(c.id + " " + m.id + " q" + (i+1) + ": нужно 4 варианта и c от 0 до 3"); });
  });
  if (c.FINAL.length !== 10) problems.push(c.id + ": в экзамене не 10 вопросов");
  c.FINAL.forEach((q, i) => { if (q.a.length < 4 || q.c >= q.a.length) problems.push(c.id + " экзамен q" + (i+1) + ": неверные варианты"); });
}
home();
console.log("Курсов:", CATALOG.length, "· уроков:", CATALOG.reduce((n,c)=>n+c.COURSE.reduce((k,m)=>k+m.lessons.length,0),0), "· ссылок:", LINKS.length);
`);
if (problems.length) { console.error(problems.join("\n")); process.exit(1); }
console.log("OK");
