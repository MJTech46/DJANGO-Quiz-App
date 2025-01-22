
# Django Quiz App

**Quiz App** is a Python-Django-based application designed for creating, managing, and taking quizzes. This application provides a user-friendly platform for administrators to add questions and quizzes and for users to participate and test their knowledge.

---

<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Warning_icon.svg/1200px-Warning_icon.svg.png"  height="270px" width="300px">

## This project is under development

</div>

# Screenshots

![img1](https://github.com/user-attachments/assets/03fae598-a4ca-454a-98ec-27560a195b88)
![img2](https://github.com/user-attachments/assets/6022f77c-0bd8-4e2c-a90e-02a0400bf32d)
![img3](https://github.com/user-attachments/assets/70562531-2ec7-44cb-9583-d08d800daefb)

## Features

### For Admins:
- **Quiz Management**: Create, update, and delete quizzes.
- **Question Management**: Add, update, and delete questions.
- **Category and Difficulty Levels**: Organize quizzes by categories and difficulty levels.
- **User Analytics**: Track user participation and performance (planned feature).

### For Users:
- **Take Quizzes**: Participate in quizzes across various topics.
- **Instant Feedback**: Get immediate results and answers after each quiz.
- **Leaderboard**: View top scorers (planned feature).
- **Account Management**: Register, log in, and manage user profiles.

---

## Installation

Follow these steps to set up the project locally:

### Prerequisites
- Python 3.8 or higher
- Django 4.0 or higher

### Steps
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/MJTech46/DJANGO-Quiz-App.git
   cd DJANGO-Quiz-App
   ```

2. **Create a Virtual Environment**  
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**  
   Update the `DATABASES` configuration in `settings.py` with your database credentials. Then, run:  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**  
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**  
   Open your browser and go to `http://127.0.0.1:8000/`.

---

## Usage

### For Admins:
1. Log in to the admin panel at `/admin`.
2. Manage quizzes and questions through the admin interface.

### For Users:
1. Register or log in to the application.
2. Browse available quizzes and participate.
3. View results and track progress.

---

## Technologies Used

- **Backend**: Django  
- **Frontend**: HTML, CSS, JavaScript (Bootstrap for responsive design)  
- **Database**: SQLite (default)   

---

## Planned Features

- User analytics and quiz performance tracking
- Time-based quizzes
- Sharing quiz results on social media
- Integration with React for a more dynamic front-end experience

---

## Contributing

Contributions are welcome! If you'd like to contribute, please:  
1. Fork the repository.  
2. Create a new branch for your feature or bug fix.  
3. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the [MIT License](LICENSE).


