USE sakila;
select *
from film;

-- 1. Tampilkan semua kolom dari tabel film (batasi 10 baris pertama).
select *
from film
limit 10;

-- 2. Tampilkan hanya kolom title dan release_year dari tabel film.
select title, release_year
from film;

-- 3. Tampilkan 5 film dengan durasi (length) terpanjang.
select title, length
from film
order by length desc
limit 5;

-- 4. Tampilkan semua film yang berdurasi lebih dari 120 menit.
select title, length
from film
where length > 120;

-- 5. Tampilkan semua film yang termasuk dalam kategori "PG-13".
select title, rating
from film
where rating = "PG-13";

-- 6. Tampilkan semua film yang dirilis pada tahun 2006.
select title, release_year
from film
where release_year = 2006;

-- 7. Tampilkan film yang memiliki durasi antara 90 dan 100 menit.
select title, length
from film
where length between 90 and 100;

-- 8. Tampilkan semua film yang memiliki rating “G”, “PG”, atau “PG-13”.
select title, rating
from film
where rating in ("G", "PG", "PG-13");

-- 9. Tampilkan film yang memiliki judul mengandung kata “LOVE” (tidak case-sensitive).
select title
from film
where title like '%love%';

-- 10. Tampilkan film yang belum memiliki deskripsi (nilai description kosong/null).
select title, description
from film
where description in (null, '')