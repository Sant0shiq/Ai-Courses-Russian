import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent; SRC = ROOT / "src"; (ROOT / "dist").mkdir(exist_ok=True)

ORDER = [
 ("claude-101","0-claude-101","start","Claude 101","Промпты, проекты, артефакты, скиллы, коннекторы и исследование. С этого стоит начать."),
 ("ai-fluency","1-ai-fluency","start","AI Fluency","Модель 4D: как делегировать задачи ИИ, описывать их и проверять результат."),
 ("ai-limits","2-limits","start","Возможности и ограничения ИИ","Как устроена модель, где она сильна и как защититься от её ошибок."),
 ("elements-of-ai","8-elements-of-ai","basics","Elements of AI","Классический курс Хельсинкского университета: поиск, вероятности, ML, нейросети, общество."),
 ("ai-for-everyone","9-ai-for-everyone","basics","AI For Everyone","Курс Эндрю Ына для не-технических специалистов: проекты на ИИ и трансформация компании."),
 ("genai-everyone","a-genai-everyone","basics","Generative AI for Everyone","Курс Эндрю Ына о генеративном ИИ: возможности LLM, RAG, дообучение, влияние на работу."),
 ("google-genai","b-google-genai","basics","Google: Introduction to Generative AI","Учебный путь Google: генеративный ИИ, большие языковые модели и ответственный ИИ."),
 ("chatgpt-pe","e-chatgpt-pe","prompt","ChatGPT Prompt Engineering for Developers","Короткий курс Эндрю Ына: принципы промптинга, итерации, обобщение, классификация, чат-бот на API."),
 ("ibm-pe","f-ibm-pe","prompt","Prompt Engineering for Everyone","Курс IBM без программирования: паттерны персоны и интервью, цепочка и дерево рассуждений."),
 ("aws-pe","g-aws-pe","prompt","Foundations of Prompt Engineering","Курс AWS: техники от few-shot до ReAct, особенности моделей, атаки на промпты, предвзятость."),
 ("claude-code","3-claude-code","build","Claude Code 101","Агентное программирование: установка, CLAUDE.md, режим планирования, скиллы, MCP."),
 ("claude-code-action","c-claude-code-action","build","Claude Code in Action","Продолжение Claude Code 101: длинные сессии, проверка, разрешения, хуки, автоматизация, плагины."),
 ("subagents","d-subagents","build","Введение в субагентов","Как делегировать работу помощникам с отдельным контекстом и проектировать их надёжно."),
 ("agentic-ai","h-agentic-ai","build","Agentic AI","Курс Эндрю Ына об агентах: рефлексия, инструменты, оценки и анализ ошибок, планирование, мультиагентность."),
 ("agent-skills","4-skills","build","Agent Skills","Как упаковать свой рабочий процесс в навык для Claude."),
 ("mcp","5-mcp","build","Введение в MCP","Открытый стандарт подключения ИИ к сервисам и данным."),
 ("platform","6-platform","dev","Claude Platform 101","Консоль, ключи, первый запрос к API, выбор модели, стоимость, ошибки."),
 ("claude-api","7-api","dev","Building with the Claude API","Диалоги, стриминг, промпты, оценка, инструменты, кэширование, RAG и агенты."),
]
TRACKS = [
 {"id":"start","t":"Старт: ИИ в работе с Claude","s":"Курсы Anthropic для всех, без технических знаний. Подходят как подготовка к Claude Academy."},
 {"id":"basics","t":"Основы ИИ","s":"Самые известные бесплатные вводные курсы других организаций. Русской версии у оригиналов нет, поэтому уроки сделаны здесь."},
 {"id":"prompt","t":"Промпт-инжиниринг","s":"Как писать запросы к моделям: курсы DeepLearning.AI, IBM и AWS. Приёмы общие для Claude, ChatGPT и других моделей."},
 {"id":"build","t":"Создатели","s":"Для тех, кто делает свои приложения и автоматизации, в том числе вайб-кодингом."},
 {"id":"dev","t":"Разработчики","s":"API и платформа для встраивания Claude в свои системы."},
]
LINKS = [
 {"name":"AI for Beginners","prov":"Microsoft","ru":"Русский","len":"12 недель · 24 урока","desc":"Основы ИИ: символьный ИИ, нейросети, компьютерное зрение, обработка текста, этика.","url":"https://github.com/microsoft/AI-For-Beginners/blob/main/translations/ru/README.md"},
 {"name":"Generative AI for Beginners","prov":"Microsoft","ru":"Русский","len":"21 урок","desc":"Создание приложений на генеративном ИИ: промпты, RAG, агенты, безопасность.","url":"https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/ru/README.md"},
 {"name":"AI Agents for Beginners","prov":"Microsoft","ru":"Русский","len":"Серия уроков","desc":"Как устроены ИИ-агенты и как их строить: инструменты, планирование, мультиагентные системы.","url":"https://microsoft.github.io/ai-agents-for-beginners/translations/ru/"},
 {"name":"ML for Beginners","prov":"Microsoft","ru":"Русский","len":"12 недель · 26 уроков","desc":"Классическое машинное обучение на Python и scikit-learn с практическими проектами.","url":"https://github.com/microsoft/ML-For-Beginners/blob/main/translations/ru/README.md"},
 {"name":"Machine Learning Crash Course","prov":"Google","ru":"Русский","len":"Интерактивный курс","desc":"Ускоренный курс машинного обучения: регрессия, классификация, данные, нейросети, эмбеддинги, LLM, ML в продакшене.","url":"https://developers.google.com/machine-learning/crash-course?hl=ru"},
 {"name":"LLM Course","prov":"Hugging Face","ru":"Частично на русском","len":"Технический","desc":"Трансформеры и большие языковые модели. На русский переведена часть глав, остальное на английском.","url":"https://huggingface.co/learn/llm-course/ru/chapter1/1"},
]

parts = []
for cid, stem, track, name, desc in ORDER:
    meta = json.loads((SRC / f"{stem}.json").read_text())
    data = (SRC / f"{stem}.js").read_text()
    qf = SRC / f"{stem}.quiz.js"
    if "const FINAL" in data: data = data[:data.index("const FINAL")]
    data += "\n" + qf.read_text() + "\nCOURSE.forEach(m=>{if(QUIZ[m.id])m.quiz=QUIZ[m.id]});\n"
    parts.append("Object.assign((function(){\n%s\nreturn {COURSE,FINAL};\n})(), %s)" % (
        data, json.dumps({"id":cid,"track":track,"name":name,"desc":desc,"meta":meta}, ensure_ascii=False)))
js = "const TRACKS=%s;\nconst LINKS=%s;\nconst CATALOG=[\n%s\n];" % (
    json.dumps(TRACKS, ensure_ascii=False), json.dumps(LINKS, ensure_ascii=False), ",\n".join(parts))
html = (ROOT / "site_template.html").read_text().replace("{{DATA}}", js)
(ROOT / "dist" / "artifact.html").write_text(html)
head, body = html.split("</style>", 1)
(ROOT / "index.html").write_text("<!doctype html>\n<html lang=\"ru\">\n<head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n" + head + "</style>\n</head>\n<body>\n" + body + "\n</body>\n</html>\n")
print(len(html)//1024, "KB")
