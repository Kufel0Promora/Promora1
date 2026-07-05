# 🚀 Promora – Strona Społeczności Discord

![Promora](https://img.shields.io/badge/Promora-Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Live-181717?style=for-the-badge&logo=github&logoColor=white)

---

## 📖 Opis projektu

**Promora** to profesjonalna strona internetowa dla społeczności Discord. Projekt łączy w sobie nowoczesny, gamingowy wygląd z pełną funkcjonalnością serwisu społecznościowego.

### ✨ Co oferuje strona?

| Funkcja | Opis |
|---------|------|
| 🔐 **Rejestracja i logowanie** | Użytkownicy rejestrują się przez ID Discord |
| ✅ **Weryfikacja Discord** | Sprawdza czy użytkownik jest na serwerze |
| 🎮 **Gra Kliker** | Klikaj, zbieraj punkty, zdobywaj rangi |
| 🏆 **Topka graczy** | Ranking najlepszych klikaczy |
| 😊 **Miły Czat AI** | Rozmowa z AI w przyjaznej atmosferze |
| 😈 **Niemiły Czat AI** | Czat, gdzie AI dogryza i roastuje |
| 📜 **Regulamin z PDF** | Podgląd i pobieranie regulaminów |
| 🛡️ **Administracja** | Lista ról i obowiązków |
| ❓ **FAQ** | Najczęściej zadawane pytania |
| 📅 **Eventy** | Kalendarz wydarzeń i historii |
| 🤖 **Bot Discord** | Resetowanie haseł przez komendy |

---

## 🔗 Linki

| Co | Adres |
|----|-------|
| **🌐 Strona (frontend)** | [https://kufel0promora.github.io/Promora1/](https://kufel0promora.github.io/Promora1/) |
| **⚙️ API (backend)** | [https://promora-backend.onrender.com/api](https://promora-backend.onrender.com/api) |
| **📦 Repozytorium** | [https://github.com/Kufel0Promora/Promora1](https://github.com/Kufel0Promora/Promora1) |
| **💬 Discord** | [discord.gg/f8qhJQSRA7](https://discord.gg/f8qhJQSRA7) |

---

## 📁 Struktura projektu
Promora1/
│
├── 📁 frontend/ # Pliki strony (na GitHub Pages)
│ ├── index.html # Strona główna
│ ├── gra.html # Gra Kliker
│ ├── regulamin.html # Regulamin z PDF
│ ├── administracja.html # Administracja
│ ├── faq.html # FAQ
│ ├── eventy.html # Eventy
│ ├── czat-mily.html # Miły czat AI
│ ├── czat-niemily.html # Niemiły czat AI
│ └── assets/ # Zasoby (CSS, JS, PDF, obrazy)
│ ├── css/
│ ├── js/
│ └── pdf/
│
├── 📁 backend/ # Backend (na Render)
│ ├── app.py # Flask API
│ ├── bot.py # Bot Discord
│ ├── config.py # Konfiguracja
│ ├── requirements.txt # Zależności Python
│ └── users.json # Baza użytkowników
│
├── 📄 README.md # Ten plik
└── 📄 .gitignore # Ignorowane pliki

text

---

## 🛠️ Technologie

### 🎨 Frontend
| Technologia | Zastosowanie |
|-------------|--------------|
| **HTML5** | Struktura strony |
| **CSS3** | Stylizacja (Dark Premium Gaming) |
| **JavaScript** | Interakcje, API, gra |
| **Google Fonts** | Czcionki |
| **Font Awesome** | Ikony |

### 🐍 Backend
| Technologia | Zastosowanie |
|-------------|--------------|
| **Python 3.10** | Język programowania |
| **Flask** | API REST |
| **discord.py** | Bot Discord |
| **bcrypt** | Haszowanie haseł |
| **requests** | Komunikacja z Discord API |

### ☁️ Hosting
| Platforma | Zastosowanie |
|-----------|--------------|
| **GitHub Pages** | Hosting frontendu |
| **Render** | Hosting backendu i bota |
| **cron-job.org** | Utrzymanie aktywności |

### 🤖 API
| API | Zastosowanie |
|-----|--------------|
| **Google Gemini AI** | Czaty AI (miły i niemiły) |
| **Discord API** | Weryfikacja użytkowników |

---

## 🎨 Styl - Dark Premium Gaming

| Element | Opis |
|---------|------|
| **Tło** | Ciemny granat (#0a0a1a) |
| **Karty** | Efekt szkła (glassmorphism) |
| **Akcenty** | Fiolet (#8B5CF6) + Błękit (#00D4FF) |
| **Przyciski** | Gradient fiolet→róż |
| **Nawigacja** | Przezroczysta, z efektem szkła |
| **Klimat** | Gamingowy z nutą elegancji |

---

## 🚀 Jak uruchomić lokalnie

### Krok 1 – Sklonuj repozytorium

```bash
git clone https://github.com/Kufel0Promora/Promora1.git
cd Promora1/backend
Krok 2 – Zainstaluj zależności
bash
pip install -r requirements.txt
Krok 3 – Stwórz plik .env
W folderze backend utwórz plik .env:

env
DISCORD_TOKEN=Twój_token_bota_z_Discord_Developer_Portal
GUILD_ID=ID_Twojego_serwera_Discord
SECRET_KEY=Losowy_klucz_do_Flaska
Krok 4 – Uruchom API
bash
python app.py
Serwer uruchomi się na http://localhost:5000

Krok 5 – Uruchom bota (opcjonalnie)
W drugim oknie CMD:

bash
python bot.py
Krok 6 – Otwórz stronę
Otwórz plik index.html w przeglądarce lub użyj Live Server w VS Code.

🤖 Komendy bota Discord
Komenda	Opis	Wymagane uprawnienia
!check_user ID	Sprawdza czy użytkownik jest na serwerze	Brak
!reset_password ID NOWE_HASLO	Resetuje hasło użytkownika	Administrator
Przykład użycia
text
!reset_password 123456789012345678 NoweHaslo123
Bot odpowie:

text
✅ Hasło dla użytkownika `123456789012345678` zostało zresetowane!
📸 Zrzuty ekranu
<!-- Wklej tutaj swoje zrzuty ekranu -->
👤 Autor
Kufel0Promora

🌐 Strona

🐙 GitHub

📝 Licencja
© 2026 B.P. Wszelkie prawa zastrzeżone.

⭐ Podziękowania
Projekt	Dzięki za
Discord.py	Biblioteka bota Discord
Google Gemini	API dla czatów AI
Render	Darmowy hosting backendu
GitHub Pages	Darmowy hosting frontendu
cron-job.org	Utrzymanie aktywności API
Font Awesome	Ikony na stronie
Google Fonts	Czcionki Inter
🚀 Status projektu
Element	Status
Frontend	✅ Online
Backend API	✅ Online
Bot Discord	✅ Online
Rejestracja	✅ Działa
Logowanie	✅ Działa
Gra	✅ Działa
Czaty AI	✅ Działają
Reset haseł	✅ Działa
📞 Kontakt
💬 Discord: Dołącz na nasz serwer tutaj

📧 Email: promora.contact@gmail.com

Stworzone z ❤️ dla społeczności Promora

text

---

## ✅ JAK DODAĆ TEN PLIK?

1. **Wejdź na swoje repozytorium GitHub**: `https://github.com/Kufel0Promora/Promora1`
2. Kliknij **"Add file"** → **"Create new file"**
3. W nazwie wpisz: `README.md`
4. **Wklej cały kod powyżej** (od `# 🚀 Promora – Strona Społeczności Discord` do końca)
5. Kliknij **"Commit new file"**

---

**Gotowe! Twój README jest teraz na GitHubie!** 😎📝🔥
