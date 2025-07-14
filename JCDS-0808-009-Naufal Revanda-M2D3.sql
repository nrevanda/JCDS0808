use world;
select * from city;
select * from country;

#SOAL JOIN
#1. Tampilkan 10 kota dengan populasi terbesar beserta nama negaranya, urutkan berdasarkan
# populasinya dari yang terbesar!

select ci.name as nama_kota, co.name as negara, co.population
from city ci, country co
where ci.countrycode = co.code
order by population desc
limit 10;

#2. Tampikan GNP negara Belanda (Netherlands), ibukota, beserta populasi dari ibukotanya!
select co.name as negara, co.gnp as GNP, ci.name as capital, ci.population
from country co, city ci
where co.capital = ci.id and co.name = "netherlands";

#3. Tampilkan 10 negara yang memiliki persentase pemakai bahasa spanyol paling tinggi!
select * from countrylanguage;
select co.name as negara, cl.percentage as presentase
from country co, countrylanguage cl
where co.code = cl.countrycode and language = "spanish"
order by percentage desc
limit 10;

#4. Tampikan GNP negara Indonesia, ibukota, populasi dari ibukotanya dan bahasa resmi yang dipakai!
select co.name as negara, co.gnp as GNP, ci.name as ibu_kota, ci.population as populasi, cl.language as bahasa
from city as ci
join country as co
on ci.id = co.capital
join countrylanguage as cl
on co.code = cl.countrycode 
where co.name = "Indonesia" and cl.isofficial = "t";

#SOAL SUBQUERY
#1 Tampilkan benua dengan jumlah negara lebih dari jumlah negara di benua North America!

-- subquery
select count(*) as jumlah_negara from country where continent = "north america";    

-- main query
select continent, count(name) as jumlah_negara
from country
group by continent
having count(name) > (select count(name) from country where continent = "north america");

#2 Tampilkan negara di Asia dengan GNP di atas rata-rata GNP negara-negara di benua Eropa,
# diurutkan dari yang terbesar!

-- subquery
select round(avg(gnp), 2) as GNP from country where continent = "europe";

-- mainquery
select name, avg(gnp) as GNP
from country
where continent = "asia"
group by name
having avg(gnp) > (select round(avg(gnp), 2) as GNP from country where continent = "europe")
order by avg(gnp) desc;

#3 Tampilkan benua berakhiran huruf 'a' dengan jumlah region lebih dari jumlah region benua Asia!
select count(distinct region) from country where continent = "asia";

select count(distinct region) as jumlah_region, continent
from country
group by continent
having jumlah_region > (select count(distinct region) from country where continent = "asia") and continent like "%a";

