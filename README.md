# 🌼 Iris Genie: AI Flower Classifier

Welcome to **Iris Genie** – your magical AI assistant for identifying iris flower species!  
Feed in your flower's measurements, and let the Genie reveal its true identity.  
Data science meets botany, with a sprinkle of fun! 🧞‍♂️✨

---

## 🎯 What Is This?

**Iris Genie** is a web app that uses a trained machine learning model to predict whether your iris is a Setosa, Versicolour, or Virginica.  
Just enter your flower’s measurements, hit the crystal ball, and get your answer—complete with emojis!🌸

---

## 🧰 Tech Behind the Magic

- **Flask**: Lightning-fast Python web framework
- **scikit-learn**: SVC model trained on the classic Iris dataset
- **Pandas**: For data wrangling
- **HTML/CSS**: Simple, responsive frontend
- **Pickle**: For model and scaler serialization

---

## 🚦 Quickstart Guide

1. **Clone this repo**  
2. Make sure you have Python 3.x installed  
3. Install dependencies:
   ```bash
   pip install flask pandas scikit-learn
   ```
4. Place `iris_model.pkl` and `scaler.pkl` in the project root  
5. Launch the Genie:
   ```bash
   python app.py
   ```
6. Open your browser at `http://localhost:5000` and start predicting!

---

## 💻 How It Works

- Enter:
  - Sepal Length (cm)
  - Sepal Width (cm)
  - Petal Length (cm)
  - Petal Width (cm)
- The app scales your input and feeds it to the AI model.
- The Genie predicts:
  - **Setosa** 🌸
  - **Versicolour** 🌺
  - **Virginica** 🌻
- If the Genie is stumped: “Unknown Species” 🤷

---

## 🖼️ User Experience

- Clean, intuitive interface
- Instant results with flower emoji flair
- Built-in measurement tips for accuracy

---

## 🌱 Sample Data

We use the famous [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris), which looks like:

| Sepal Length | Sepal Width | Petal Length | Petal Width | Species     |
|--------------|-------------|--------------|-------------|-------------|
| 5.1          | 3.5         | 1.4          | 0.2         | setosa      |
| 6.7          | 3.0         | 5.2          | 2.3         | virginica   |
| 5.9          | 3.0         | 5.1          | 1.8         | virginica   |

---

## 📝 Example Prediction

> Input: Sepal Length: 6.4, Sepal Width: 2.8, Petal Length: 5.6, Petal Width: 2.2  
> Output: **Your 🌻 is Virginica!**

---

## 💡 Flower Measurement Tips

- **Sepal**: Outer, usually green part
- **Petal**: Colorful inner part
- Typical ranges:
  - Length: 4–8 cm
  - Width: 2–4 cm

---

## 🤝 Want to Contribute?

- Fork the repo
- Make your magic
- Open a pull request


---

## 🙏 Credits

- Powered by Flask, scikit-learn, and the UCI Iris dataset
- UI inspired by minimalist design and botany books
- Genie character by your imagination 🧞‍♂️

---

> _“Let the Genie guide your garden!”_ 🌼

---

**Maintained by Bibin Shan**  

**📬 Contact & Networking**
- 📧 Email: iambibinshan@email.com
- 🔗 LinkedIn: linkedin.com/in/bibin-shan
- 🐦 X (Twitter): @bibin_shan
- 📸 Instagram: @bibin_shan

Questions? Open an issue or rub the lamp! 🪔



