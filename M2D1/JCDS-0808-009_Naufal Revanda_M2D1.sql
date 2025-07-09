## Exercise 1 SQL

USE world;
SHOW FULL TABLES;
SELECT * FROM country;

# 1.  Ada berapa negara di database world?
select count(distinct name) as jumlah_negara
from country;

# 2.  Tampilkan rata-rata harapan hidup di benua Asia!
select avg(LifeExpectancy) as rata2_harapan_hidup_Asia
from country
where continent = "Asia";

# 3.  Tampilkan total populasi di Asia Tenggara!
select sum(population) as populasi_asia_tenggara
from country
where region = "southeast asia";

# 4.  Tampilkan rata-rata GNP di benua Afrika region Eastern Africa. 
# Gunakan alias 'Average_GNP' untuk rata-rata GNP!
select avg(GNP) as Average_GNP
from country
where region = "eastern africa";

# 5.  Tampilkan rata-rata Populasi pada negara yang luas areanya lebih dari 5 juta km2! 
select avg(population)
from country
where surfacearea > 5000000;

# 6.  Ada berapa bahasa (unique) di dunia?
select * from countrylanguage;
select count(distinct language) 
from countrylanguage;
-- Jumlah bahasa unik: 457

# 7.  Tampilkan GNP dari 5 negara di Asia yang populasinya di atas 100 juta penduduk!
select name, gnp
from country
where continent = "asia" and population > 100000000
limit 5;

# 8.  Tampilkan negara di Afrika yang memiliki SurfaceArea di atas 1.200.000!
select name, continent, surfacearea
from country
where continent = "africa" and surfacearea > 1200000;

# 9.  Tampilkan negara di Asia yang sistem pemerintahannya adalah republik. 
# Ada berapa jumlah negaranya?
-- 1. list negara sistem pemerintahan republik
select name, continent, governmentform
from country
where continent = "asia" and governmentform = "republic";
-- 2. jumlah negaranya
select count(distinct name) as jumlah_negara_republik
from country
where continent = "asia" and governmentform = "republic";

# 10. Tampilkan jumlah negara di Eropa yang merdeka sebelum 1940!
select name, continent, indepyear
from country
where continent = "europe" and indepyear < 1940



