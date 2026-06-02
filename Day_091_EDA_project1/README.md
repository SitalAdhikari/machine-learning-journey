## Day 91: Exploratory Data Analysis (EDA)
Today, I initiated the **Exploratory Data Analysis (EDA)** phase for the Student Performance Prediction project to understand the underlying structure, distributions, and relationships within our dataset.
### Key Learnings
 * **Initial Data Inspection**: Loaded the student dataset and verified feature shapes, capturing structural variables like gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, and performance markers like math_score.
 * **Categorical Value Profiling**: Investigated unique categorical groupings to check data diversity, mapping out classification levels such as parental degree types (bachelor's degree, some college, master's degree) and lunch categories (standard, free/reduced).
 * **Feature Classification Automation**: Programmed automated column segregators using df.select_dtypes() to separate numerical features from categorical features automatically:
   * num_cols: Numerical features isolated via include=np.number.
   * cat_cols: Categorical features isolated via exclude=np.number.
Day 91 complete—data profile mapped and ready for visualization! 🚀
