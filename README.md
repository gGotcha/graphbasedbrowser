
Я хотел бы иметь для ежедневной работы on-line editable graph based data browser. Что-то вроде <a href='https://neo4j.com/developer/guide-neo4j-browser/'>neo4j browser</a> + <a href = 'https://www.freeplane.org/wiki/index.php/Main_Page'>freeplane<a> в виде браузерного приложения. Вместе с эти я хотел разобраться с d3js библиотекой, Flask, Mongodb, Neo4j.  
Здесь публикую скорее эксперименты, чем проект. Так же это своего рода портфолио на тему того, что я могу, а, иногда, даже люблю разрабатывать.
Ввиду экспериментальности сделано всё не в духе best practice. Буду править по мере ознакомления с ними. Стройность мыслей и цели предлагаю смотреть в <a href='https://github.com/gGotcha/graphbasedbrowser/blob/master/others/Feature'>feature request</a>

Техническое
- Предполагается, что граф должен сохраняться в neo4j базу. На данный момент испоьзуется pgsql, собрать граф можно из таблицы. Так же хотел изучить возможности Mongodb, на текущий момент у нее есть модуль обхода графа.  
- API и веб сервер - Flask.
- D3js,JQuery. 

О том зачем нам нужен  on-line editable graph based data browser можно почитать <a href='https://github.com/gGotcha/graphbasedbrowser/blob/master/others/WhyWeNeedIt'>здесь</a>

<a href='https://github.com/gGotcha/graphbasedbrowser/blob/master/others/Bugs'>Баги</a> и <a href='https://github.com/gGotcha/graphbasedbrowser/blob/master/others/Feature'>Фичи</a> 
   
https://graphbasedbrowser.herokuapp.com
'Heroku free' тариф стартует контейнер через 15 сек., поэтому, просьба, подождать. 
