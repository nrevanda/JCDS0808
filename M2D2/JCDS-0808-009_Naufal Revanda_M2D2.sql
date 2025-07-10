# Exercise M2_S2

# World
USE world;
select * from country;

#1. Ada berapa region di database world? Ubah headernya menjadi 'Jumlah_Region'!
select count(distinct region) as 'Jumlah_Region'
from country;
-- ada 25 region

#2. Ada berapa negara di Africa? Ubah headernya menjadi 'Jumlah_Negara'!
select count(distinct name) as 'Jumlah_negara'
from country
where continent = 'africa';
-- ada 58 negara di africa

#3. Tampilkan 5 negara dengan populasi terbesar! Ubah headernya menjadi 'Nama_Negara' dan 'Populasi'!
select name as 'Nama_Negara', population as 'Populasi'
from country
order by Populasi desc
limit 5;

#4. Tampilkan rata-rata harapan hidup tiap benua dan urutkan dari yang terendah! 
# Ubah headernya menjadi 'Nama_Benua' dan 'Rata_Rata_Harapan_Hidup'!
select continent as 'Nama_Benua', avg(lifeexpectancy) as 'Rata_Rata_Harapan_Hidup'
from country
group by Nama_Benua
order by Nama_Benua asc;

#5. Tampilkan Jumlah region tiap benua dengan jumlah region lebih dari 3! 
# Ubah headernya menjadi 'Nama_Benua' dan 'Jumlah_Region'!
select continent as Nama_Benua, count(region) as Jumlah_Region
from country
group by continent
having Jumlah_Region > 3;

#6. Tampilkan rata-rata GNP di Afrika berdasarkan regionnya 
# dan urutkan dari rata-rata GNP terbesar! 
# Ubah headernya menjadi 'Nama_Region' dan 'Rata_Rata_GNP'!
select region as Nama_Region, avg(gnp) as Rata_Rata_GNP
from country
where continent = 'africa'
group by region
order by Rata_Rata_GNP desc;

#7. Tampilkan negara di Eropa yang memiliki nama dimulai dari huruf I
select name from country
where name like 'i%' and continent = 'europe';

#8. Tampilkan Jumlah bahasa tiap negara! Urutkan dari yg paling banyak! 
# Ubah headernya menjadi 'Jumlah_Bahasa'
select * from countrylanguage;
select countrycode, count(distinct language) as jumlah_bahasa
from countrylanguage
group by countrycode
order by jumlah_bahasa desc;

#9. Tampilkan nama negara yang panjang hurufnya 6 huruf dan berakhiran 'O'
select name from country
where name like '_____o';


#10. Tampilkan 7 bahasa terbesar di Indonesia 
# (secara persentase, dengan persentase yg dibulatkan)! 
# Ubah headernya menjadi 'Bahasa' dan 'Persentase'
select countrycode, language as bahasa, round(percentage, 0) as presentase
from countrylanguage
where countrycode = 'IDN'
order by presentase desc
limit 7;

#11. Tampilkan Continent yang memiliki GovernmentForm kurang dari 10
select continent, count(governmentform)
from country
group by continent
having count(governmentform) < 10;

#12. Region mana saja yg Total GNP-nya mengalami kenaikan dari Total GNP sebelumnya (GNPOld)? 
# Urutkan dari yg tertinggi!
select region, gnp, gnpold
from country
where GNP > GNPOld
order by GNP desc;




