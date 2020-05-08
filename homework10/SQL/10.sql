-- ⑩ 按照性别来进行人员分组如下显示（group by + group_concat()）；
--  | 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                             |
-- 	| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                   |
-- 	| 中性   | 金星                                                       |
--  | 保密   | 凤姐                                                       |
SELECT gender,GROUP_CONCAT(name)
FROM students
GROUP BY gender