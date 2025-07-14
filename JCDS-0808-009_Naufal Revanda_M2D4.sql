# NO.1
use sakila;
show tables;

select * from film;
select * from film_category;
select * from category;
 
 -- tabel 1= rata-rata rental_duration keseluruhan
with
avg_rental as (
	select avg(rental_duration) as avg_duration 
	from film),
    
    -- tabel 2= rental duration per kategori
category_duration as (
	select  c.name,
    sum(f.rental_duration) as total_rental_duration
from film_category fc
join film f on fc.film_id = f.film_id
join category c on fc.category_id = c.category_id
join avg_rental ar on f.rental_duration <= ar.avg_duration
group by c.name
)

-- final
select 
	name,
    total_rental_duration,
	sum(total_rental_duration) over(rows between unbounded preceding and current row) as cumulative_sum,
	avg(total_rental_duration) over(rows between unbounded preceding and current row) as moving_avg
from category_duration
order by total_rental_duration desc
limit 5;


#NO.2
use sakila;
show tables;

select rating,
    avg(rental_duration) from film
	group by rating;


#Langkah 1, mencari 3 kategori dengan film terbanyak
select
	fc.category_id, c.name,
    count(fc.category_id) jumlah_film
from category as c
join film_category as fc
on c.category_id = fc.category_id
group by  fc.category_id, c.name
order by jumlah_film desc
limit 3;

#Langkah 2, menghitung avg_rental_duration dari setiap rating dari film dengan kondisi di Langkah 1
select
	f.rating,
    avg(f.rental_duration) as avg_rental_duration
from film f
join film_category fc
on f.film_id = fc.film_id
where fc.category_id in ("8", "9", "15")
group by f.rating
order by avg_rental_duration desc;


#NO. 3
use sakila;
show tables;
select * from inventory;


#Langkah 1 membuat tabel total rent per filmnya
with total_rental_per_film as (
select 
	f.title,
    count(r.customer_id) as total_customer
from rental as r
join inventory as i on r.inventory_id = i.inventory_id
join film as f on i.film_id = f.film_id
group by f.title
),

#Langkah 2 membuat tabel rata2 customer dari tabel langkah1
avg_rental as (
	select avg(total_customer) as avg_customer
	from total_rental_per_film
)

#Langkah 3 menggabungkan kedua tabel untuk mengambil nilai yang diinginkan
select
	t.title,
    t.total_customer
from total_rental_per_film as t
join avg_rental as ar on t.total_customer > ar.avg_customer
where
	(t.title like 'C%' or t.title like 'G%')
    and t.total_customer between 15 and 25
group by t.title;
