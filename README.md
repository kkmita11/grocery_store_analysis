# Analiza sprzedaży detalicznej – raport Power BI  
*(English version below)*

## 📌 Cel projektu
Celem projektu była analiza danych sprzedażowych sklepu spożywczego z 2018 roku oraz prezentacja wyników w formie interaktywnego raportu Power BI.  
Projekt pokazuje przygotowanie danych w **Pythonie (Pandas)**, modelowanie i obliczenia w **Power BI (DAX)** oraz projektowanie raportu pod kątem wniosków biznesowych.  

---

## 📊 Opis danych
- **Źródło**: [Kaggle – Total Sale 2018 Yearly Data of Grocery Shop](https://www.kaggle.com/datasets/agatii/total-sale-2018-yearly-data-of-grocery-shop)  
- **Zakres**: Sprzedaż za rok 2018. Sprzedaż produktów zagregowana w ramach miesiąca (⚠️ nie dane dzienne).  
  **Brak danych za ostatni tydzień roku: 25.12 – 31.12.2018.**  
- **Zawartość**: dwa pliki CSV zawierające m.in.:
  - Data (miesiąc, rok)  
  - Nazwa produktu i kategoria  
  - Ilość sprzedanych sztuk  
  - Wartość sprzedaży brutto  
  - Marża  

Dane zostały oczyszczone i przekształcone w Pythonie (Pandas), a następnie załadowane do Power BI.  

⚠️ **Uwaga**: Zauważono rozbieżność (~0,7%) między sumą miesięczną a dzienną (pomiędzy plikami). Najprawdopodobniej wynika to z różnic w agregacji i/lub zaokrągleniach w źródłowych raportach. Różnica nie ma istotnego wpływu na wnioski analityczne.  

---

## 📑 Opis raportu
Raport Power BI składa się z dwóch stron:

### 1. Sprzedaż w ciągu roku, analiza produktów i kategorii
- Trendy sprzedaży i marży w ujęciu dziennym i miesięcznym  
- Najlepiej sprzedające się kategorie i produkty w ujęciu **miesięcznym i rocznym**  
- Top produkty według wybranego kryterium (ilość, marża, sprzedaż)  
- Karty KPI z podsumowaniami sprzedaży i rentowności  

### 2. Sprzedaż w niedziele i w ciągu tygodnia
- Sprzedaż w podziale na dni tygodnia  
- Wpływ ustawy o handlu w niedziele na wyniki sprzedażowe  
- Udział niedziel niehandlowych w sprzedaży rocznej (sklep ma możliwość sprzedaży w niedziele niehandlowe)  

---

## 📈 Najważniejsze wnioski (przykłady)
- Największy udział w wypracowanej marży mają: Piwo, Warzywa, Nabiał i Chleb – łącznie ~41% całkowitej marży.  
- Papierosy generują największy udział w przychodach (~21%), ale tylko ~6% w marży.  
- Sobota generuje największą sprzedaż (19%), niedziela najmniejszą (11%).  
- Sprzedaż w niedziele niehandlowe to ok. 7% rocznej sprzedaży – przewaga konkurencyjna. Planowane przez rząd ograniczenie liczby niedziel handlowych uwydatni przewagę sklepu.  
- Średnia dzienna sprzedaż w rekordowym miesiącu – sierpniu – wynosiła 3784 zł i była o 32% wyższa niż w najsłabszym styczniu. Prawdopodobnie grudzień był najlepszy, ale brakuje danych z ostatniego tygodnia.  
- Sprzedaż napojów alkoholowych stanowi 19% wypracowanej marży.  

---

## 🛠 Wykorzystane narzędzia
- **Python (Pandas)** – przygotowanie danych  
- **Power BI Desktop** – modelowanie i wizualizacja  
- **DAX** – miary analityczne  

---

## ⚖️ Licencja i wykorzystanie danych
- Źródło danych: Kaggle (`Data files © Original Authors`).  
- Szczegóły licencji nie są jasne – nie wiadomo, czy wolno dalej dystrybuować pliki.  
- Dlatego pliki CSV **nie są zawarte** w repozytorium.  
- Dane można pobrać bezpośrednio z Kaggle: [link](https://www.kaggle.com/datasets/agatii/total-sale-2018-yearly-data-of-grocery-shop).  

---

# Retail Sales Analysis – Power BI Report  

## 📌 Project Goal
The goal of this project was to analyze grocery store sales data from 2018 and present the results in an interactive Power BI report.  
The project demonstrates data preparation in **Python (Pandas)**, modeling and calculations in **Power BI (DAX)**, and dashboard design for business insights.  

---

## 📊 Data Description
- **Source**: [Kaggle – Total Sale 2018 Yearly Data of Grocery Shop](https://www.kaggle.com/datasets/agatii/total-sale-2018-yearly-data-of-grocery-shop)  
- **Coverage**: Sales for 2018, aggregated at the product level by month (⚠️ not daily transactions).  
  **Data for the last week of the year (25.12 – 31.12.2018) is missing.**  
- **Content**: Two CSV files including:
  - Date (month, year)  
  - Product name and category  
  - Quantity sold  
  - Gross sales value  
  - Margin  

Data was cleaned and transformed in Python (Pandas) before being loaded into Power BI.  

⚠️ **Note**: A discrepancy (~0.7%) was observed between monthly and daily totals (between files). This likely results from aggregation and/or rounding differences in the original reports. The discrepancy does not materially affect analytical conclusions.  

---

## 📑 Report Description
The Power BI report consists of two pages:

### 1. Yearly sales, products and categories analysis
- Daily and monthly sales and margin trends  
- Top-selling categories and products (monthly and yearly)  
- Top products by selected metric (quantity, margin, sales)  
- KPI cards summarizing sales and profitability  

### 2. Sunday and weekly sales
- Sales by day of the week  
- Impact of the Sunday trade ban on sales performance  
- Share of non-trading Sundays in annual sales (this store is allowed to sell on non-trading Sundays)  

---

## 📈 Key Insights (examples)
- Beer, Vegetables, Dairy, and Bread account for ~41% of total margin.  
- Cigarettes generate ~21% of revenue but only ~6% of margin.  
- Saturday is the strongest sales day (19%), Sunday the weakest (11%).  
- Non-trading Sundays account for ~7% of annual sales – a competitive advantage. Planned government restrictions on trading Sundays highlight this advantage.  
- In the strongest month (August), average daily sales were PLN 3784, 32% higher than in the weakest month (January). December was likely the peak month, but the last week’s data is missing.  
- Alcoholic beverages account for 19% of total margin.  

---

## 🛠 Tools & Technologies
- **Python (Pandas)** – data preparation  
- **Power BI Desktop** – modeling and visualization  
- **DAX** – analytical measures  

---

## ⚖️ License & Data Usage
- Dataset source: Kaggle (`Data files © Original Authors`).  
- License details are unclear – redistribution may not be explicitly allowed.  
- Therefore, CSV files are **not included** in the repository.  
- Data can be accessed directly from Kaggle: [link](https://www.kaggle.com/datasets/agatii/total-sale-2018-yearly-data-of-grocery-shop).  
