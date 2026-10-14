# ИИ-курсы на русском

Одностраничный сайт для подготовки к официальным бесплатным курсам по ИИ — для тех, кто не знает английский.

На главной — библиотека курсов по трекам. Каждый курс открывается на той же странице: уроки на русском, тест после каждого модуля, итоговый экзамен (проходной балл 80%) и учебный сертификат. Прогресс хранится в браузере. Для курсов, у которых уже есть русская версия, даны прямые ссылки.

## Курсы

| Трек | Курс | Оригинал |
|---|---|---|
| Старт | Claude 101, AI Fluency, Возможности и ограничения ИИ | Anthropic · Claude Academy |
| Основы ИИ | Elements of AI | University of Helsinki |
| Основы ИИ | AI For Everyone, Generative AI for Everyone | DeepLearning.AI |
| Основы ИИ | Introduction to Generative AI | Google Cloud |
| Промпт-инжиниринг | ChatGPT Prompt Engineering for Developers | DeepLearning.AI |
| Промпт-инжиниринг | Prompt Engineering for Everyone | IBM Skills Network |
| Промпт-инжиниринг | Foundations of Prompt Engineering | AWS Skill Builder |
| Создатели | Claude Code 101, Claude Code in Action, Введение в субагентов, Agent Skills, Введение в MCP | Anthropic · Claude Academy |
| Создатели | Agentic AI | DeepLearning.AI |
| Разработчики | Claude Platform 101, Building with the Claude API | Anthropic · Claude Academy |

Ссылки на русские версии: Microsoft AI / Generative AI / AI Agents / ML for Beginners, Google Machine Learning Crash Course, Hugging Face LLM Course.

## Структура

```
src/
  <курс>.json      — название, описание, ссылка на оригинал, данные сертификата
  <курс>.js        — уроки (const COURSE = [...])
  <курс>.quiz.js   — тесты модулей и итоговый экзамен (QUIZ, FINAL)
site_template.html — движок сайта: главная, просмотр курса, тесты, сертификат
build.py           — собирает всё в index.html
index.html         — готовый сайт (можно открыть в браузере или выложить на GitHub Pages)
```

## Сборка

```bash
python3 build.py   # собрать index.html
node check.js      # открыть каждый шаг каждого курса и проверить тесты
```

Порядок курсов, треки и внешние ссылки задаются в начале `build.py` (`ORDER`, `TRACKS`, `LINKS`).

### Как добавить курс

1. Создать в `src/` три файла: `<id>.json`, `<id>.js`, `<id>.quiz.js` по образцу существующих.
2. В каждом модуле 3 вопроса, в экзамене 10, у каждого вопроса 4 правдоподобных варианта. Поле `c` — индекс правильного ответа (порядок вариантов на сайте перемешивается).
3. Добавить строку в `ORDER` в `build.py` и запустить сборку.

## Важно

Уроки написаны заново на русском по открытым программам курсов. Это не официальные курсы и не переводы материалов Anthropic, Google, DeepLearning.AI, Хельсинкского университета или других организаций. Сертификаты на сайте учебные; официальные сертификаты выдаются только на сайтах оригинальных курсов.
