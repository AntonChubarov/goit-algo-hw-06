# ДЗ Графи

У якості графу для досліджень взято [Les Miserables](https://websites.umich.edu/~mejn/netdata/):
coappearance network of characters in the novel Les Miserables[1] (роман В. Гюго "Знедолені").

## Висновки

1. Отриманий досвід роботи з графами за допомогою бібліотеки NetworkX;
2. Аналіз ступенів вершин дозволяє легко визначити центральних персонажів роману;
3. На графі BFS превалюють "радіальні" ребра, оскільки алгоритм відвідує всі сусіди поточного рівня перед переходом до наступного;
4. На графі DFS превалюють "глибокі ланцюги", оскільки алгоритм просувається глибше, перш ніж рухатися "в боки";

### Посилання

1. D. E. Knuth, The Stanford GraphBase: A Platform for Combinatorial Computing, Addison-Wesley, Reading, MA (1993).
