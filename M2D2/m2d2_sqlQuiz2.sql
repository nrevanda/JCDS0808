-- Evaluasi Kategori Negara Berdasarkan Populasi dan Harapan Hidup
-- Database: world
-- Tabel: country
-- Konteks: Sebagai seorang Data Analyst di organisasi internasional, kamu diminta mengelompokkan negara-negara berdasarkan 
--          populasi dan harapan hidup serta menilai kelompok negara mana yang memiliki stabilitas demografis yang lebih baik.

/* Deskripsi
Tampilkan data agregat berdasarkan kategori berikut:
1. pop_group:
	- 'Small' untuk populasi < 1 juta
    - 'Medium' untuk populasi 1–50 juta
    - 'Large' untuk populasi > 50 juta

2. life_status:
	- 'High' jika life expectancy ≥ 75
    - 'Moderate' jika antara 60–74.9
    - 'Low' jika < 60

3. Hitung:
	- Jumlah negara (total_negara)
    - Rata-rata life expectancy (avg_life_exp)
    - Rata-rata GNP (avg_gnp)

4. Filter hanya kombinasi kategori yang punya rata-rata harapan hidup di atas 78 tahun

5. Urutkan berdasarkan jumlah negara terbanyak */

-- Your Code Here ...

use world;
select * from country;

select
	case
    when population < 1e6 then "Small"
    when population between 1e6 and 50e6 then "Medium"
    else "Large"
	end as pop_group,
    
    case
    when lifeexpectancy >= 75 then "High"
    when lifeexpectancy between 60 and 74.9 then "Moderate"
    else "Low"
    end as life_status,
    
    count(name) as total_negara, avg(LifeExpectancy) as avg_life_exp, avg(GNP) as avg_gnp
    
from country
group by pop_group, life_status
having avg_life_exp > 78
order by total_negara desc;

