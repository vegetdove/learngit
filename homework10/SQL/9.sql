-- ⑨ 分别统计性别为男/女的人年龄平均值
SELECT * FROM
(SELECT gender,AVG(age) 
FROM students 
GROUP BY gender)
AS total
WHERE gender = "男" or gender = "女"
