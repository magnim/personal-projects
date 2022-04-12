import random

dice_dic = {
1 : '''
 _          _
|           |
|     *     |
|_         _| ''',
2 : '''
 _          _
|     *     |
|           |
|_    *    _| ''',
3 : '''
 _          _
|     *     |
|     *     |
|_    *    _| ''',
4 : '''
 _          _
| *      *  |
|           |
|_*      * _| ''',
5 : '''
 _          _
| *      *  |
|     *     |
|_*      * _| ''',
6 : '''
 _          _
| *      *  |
| *      *  |
|_*      * _| '''}

roll = True

while roll:
    rolling = random.randint(1,6)
    print(dice_dic[rolling])
    another_roll = input("do you wish to roll again? (y/n): ").lower()
    if another_roll == 'y':
        continue
    else:
        roll = False