# Exploring Transfer Learning and Seeded Iterated Learning for Multilingual Text Classification Using AfriBERTA

### Step 1: Setting Up the Environment

1.  Install necessary libraries, including the [HuggingFace Transformers](https://huggingface.co/transformers/) library, for working with AfriBERTA.
2.  Load the pre-trained AfriBERTA base model.

### Step 2: Data Preprocessing

1.  Choose two text classification tasks from the [OSCAR corpus](https://oscar-corpus.com/), and download the relevant data.

-   [x] Choose two text classification in different African languages from available sources such as the one above.

2.  Preprocess the data for each task, including tokenization and encoding.

-   [x] Preparing train-validation-test splits for each task while avoiding data leaks.

### Step 3: Fine-tuning AfriBERTA without SIL

1.  Fine-tune AfriBERTA on each task separately, without using SIL.

-   [x] fine-tune AfriBERTA on the first text classification task using cross-entropy loss and softmax output

2.  Evaluate the model's performance on the test et using appropriate metrics (accuracy, F1 score, etc.)
3.  Report the results and note any overfitting or limitations.

### Step 4: Fine-tuning AfriBERTA with SIL

1.  Implement seeded iterated leaning (SIL) with the modified version for text classification tasks.
2.  Use the teacher model from Step 3 to seed the SIL process.

-   [x] Use the the teacher model (AfriBERTA) to generate soft labels for the student model.

3.  Fine-tune the student model on the second text classification task using soft labels and cross-entropy loss.
4.  Evaluate the student model's performance on the test set using appropriate metrics (accuracy, F1 score, etc.)
5.  Report the results and compare them to the baseline model (fine-tuned AfriBERTA without SIL).

### Step 5: Exploring the Effects of SIL (Analysis of SIL Benefits)

1.  Compare the performance of the student model with and without SIL.
2.  Analyze the impact of SIL on avoiding language/drift for the first fine-tuning task and learning the second task.
3.  Use Approximate Bayesian Computation (ABC) to compare the student model's performance with and without SIL.

-   [x] Use appropriate metrics and interpretation techniques to assess benefits and detriments.

4.  Report the results and discuss the findings, including whether SIL was helpful or not.

### Step 6: Write Up

1.  Prepare a report detailing the steps taken and the results obtained.
2.  Include sections such as Introduction, Background, Methodologyy(describing the SIL approach), Results, Discussion(including insights into SIL's impact), and Conclusion.
3.  Present appropriate figures, table, metrics in the report.
4.  Discuss limitations, challenges, and potential areas for future research.
5.  Be sure to cite all relevant sources and include a list of references.

### Project Timeline

-   [x] Week 1: Project Proposal
-   [x] Week 2: Environment Setup ✅
-   [x] Week 3: Data Preprocessing ⏳
-   [x] Week 4: Fine-tuning AfriBERTA without SIL
-   [x] Week 5: Fine-tuning AfriBERTA with SIL
-   [x] Week 6: Exploring the Effects of SIL (Analysis of SIL Benefits)
-   [x] Week 7: Write Up
-   [x] Week 8: Final Report

### Project Proposal

-   [x] Project Title: Exploring Transfer Learning and Seeded Iterated Learning for Multilingual Text Classification Using AfriBERTA
-   [x] Project Description: This project aims to explore the use of seeded iterated learning (SIL) for multilingual text classification using AfriBERTA, a pre-trained language model for African languages. SIL is a transfer learning approach that uses a teacher model to generate soft labels for a student model. The student model is then fine-tuned on the second task using the soft labels and cross-entropy loss. The goal is to compare the performance of the student model with and without SIL and analyze the impact of SIL on avoiding language drift for the first fine-tuning task and learning the second task. The project will use the [HuggingFace Transformers](https://huggingface.co/transformers/) library for working with AfriBERTA and the [OSCAR corpus](https://oscar-corpus.com/) for the text classification tasks. The project will be implemented in Python using Vscode.
-   [x] Project Goals: The goal of this project is to explore the use of seeded iterated learning (SIL) for multilingual text classification using AfriBERTA, a pre-trained language model for African languages. The project will use the [HuggingFace Transformers](https://huggingface.co/transformers/) library for working with AfriBERTA and the [OSCAR corpus](https://oscar-corpus.com/) for the text classification tasks. The project will be implemented in Python using Google Colab.
-   [x] Project Deliverables: The project will deliver a report detailing the steps taken and the results obtained. The report will include sections such as Introduction, Background, Methodology(describing the SIL approach), Results, Discussion(including insights into SIL's impact), and Conclusion. The report will present appropriate figures, table, metrics. The report will discuss limitations, challenges, and potential areas for future research. The report will cite all relevant sources and include a list of references.
-   [x] Project Timeline: The project will be completed in 8 weeks. The first week will be spent on the project proposal. The second week will be spent on environment setup. The third week will be spent on data preprocessing. The fourth week will be spent on fine-tuning AfriBERTA without SIL. The fifth week will be spent on fine-tuning AfriBERTA with SIL. The sixth week will be spent on exploring the effects of SIL (analysis of SIL benefits). The seventh week will be spent on the write-up. The eighth week will be spent on the final report.
-   [x] Project Team: The project will be completed by a single person.
-   [x] Project References: The project will use the [HuggingFace Transformers](https://huggingface.co/transformers/) library for working with AfriBERTA and the [OSCAR corpus](https://oscar-corpus.com/) for the text classification tasks. The project will be implemented in Python using Vscode.

### Project Progress:

![](https://img.shields.io/badge/status-In_progress-yellow.svg)