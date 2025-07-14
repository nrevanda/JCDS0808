
-- ************************************************************
-- [SAKILA] Top 3 Film Terlaris per Kategori
-- Tujuan: Temukan 3 film dengan pendapatan tertinggi per kategori
-- Teknik: CTE, JOIN, Window Function (RANK)
-- ************************************************************

/* Deskripsi 
Manajemen ingin mengetahui 3 film dengan total pendapatan tertinggi di tiap kategori film.
Anda diminta menyusun laporan:
- Gabungkan transaksi pembayaran dengan film dan kategorinya
- Hitung total pendapatan per film
- Gunakan window function untuk mencari 3 film terlaris di setiap kategori (tanpa LIMIT) */

/* 3 Query
1. Menghitung total revenue dari tiap film (multi table)
2. Bikin ranking setiap film di setiap kategori berdasarkan total revenue (Query 1)
3. Filter (Query 2) ranking <= 3 */

use sakila;
show tables;
select * from film;
select * from sales_by_film_category;
select * from payment;
select * from rental;
select * from category;
select * from film_category;
select * from inventory;

with revenue_film as (
select f.title, c.name as category, sum(p.amount) as revenue
from payment p
join rental r on p.rental_id = r.rental_id
join inventory i on r.inventory_id = i.inventory_id
join film_category fc on i.film_id = fc.film_id
join category c on fc.category_id = c.category_id
join film f on fc.film_id = f.film_id
group by f.title, c.name, f.film_id
order by revenue desc
),

ranked_revenue as(
select category, title, revenue,
		row_number() over(partition by category order by revenue desc) as RN
from revenue_film
)

select *
from ranked_revenue
where RN <= 3
order by category, RN;



