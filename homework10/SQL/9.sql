-- ⑨ 分别统计性别为男/女的人年龄平均值
SELECT gender,AVG(age) 
FROM students 
GROUP BY gender
LIMIT 2