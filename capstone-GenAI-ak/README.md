# AI-Based Generative QA System
## 1. Email Subject Line Generation

### Problem Description
The task is to generate concise email subject lines from the body of the email. This involves identifying the most salient sentences and summarizing them into a few words.

### Dataset
We have used the dataset from [Github AESLC.](https://github.com/ryanzhumich/AESLC)

The dataset is annotated Enron Subject Line Corpus. It has dev, test, and train email datasets.
* Cleaned, filtered, and deduplicated emails from the Enron Email Corpus. 
* Sizes of train/dev/test splits: 14,436 / 1,960 / 1,906
* Average email length: 75 words
* Average subject length: 4 words

Dev and test datasets have @subject, @ann0,@ann1, and @ann2 to represent the subject lines of the mail.   
The train dataset has @subject as the subject line. 

**Train Data**  

![alt text](https://github.com/ch22group16/email_sub_generation/blob/main/dataset/Train.JPG)

**Test Data**  

![alt text](https://github.com/ch22group16/email_sub_generation/blob/main/dataset/Test.JPG)


### Data preprocessing

We have considered the below points to preprocess the data. 
* Removed unnecessary spaces with single space.
* Removed non-word and non-space characters.
* Extracted the content before @subject as email_body
* Extracted @subject as subject_line, @ann0 as subject_line1, @ann1 as subject_line2, and @ann2 as subject_line3.
* Created a single data file for dev, test, and train data with columns email_body, subject_line, subject_line1, subject_line2, subject_line3 contents.

We have analyzed the email body. The average email body has 2500 characters.  
To train the dataset, we have only considered the first 2500 characters of the email body from each email.


### Models
We have used the below models to train and test the data.

|   Model  | Training Notebook |
|----------|-------------------|
| BART | [Capstone_Group_16_BART_WandB.ipynb](https://github.com/ch22group16/capstone-GenAI/blob/main/Capstone_Group_16_BART_WandB.ipynb)|
| T5 small | [email_sub_gen_T5_small.ipynb](https://github.com/ch22group16/capstone-GenAI/blob/main/email_sub_gen_T5_small.ipynb) |
| Distill GPT2 | [Capstone_Group_16_DistilGPT2_WandB.ipynb](https://github.com/ch22group16/capstone-GenAI/blob/main/Capstone_Group_16_DistilGPT2_WandB.ipynb) |
| GPT2 | [email_sub_gen_gpt2_latest.ipynb] (https://github.com/ch22group16/capstone-GenAI/blob/main/email_sub_gen_gpt2_latest.ipynb) |

### Zero Shot Testing
We performed Zero Shot testing in all the models we tried. The common trend that we noticed was long subject lines. Therefore, we focussed on hyper parameters such as length_penalty, max_new_tokens, max_length, min_length and num_beams

For Example:

**Email Body:** _Hi Judy How are you I sent Ingrid an email and she told me that you are still at Enron Thats good I tried to call you at work but the girl that answered the phone said that you were on vacation today How are the kids and Rob I think about you all of the time Ingrid told me that she told you that I got married It isnt Tod it is James Johnson that I dated in high school We could have saved each other a lot of heart ache and just stayed together He is really sweet He has 3 boys so now there are 4 boys in my house I am real outnumbered But its fun Are you still working parttime or fulltime There is so much to talk about we need to get together for lunch or something Maybe we could meet somewhere one day let me know My phone numbers are Home 2818073186 and work 7132154473 And now you have my email address Talk to you soon Laurie_

**Subject Line:** _Latest Marketing List_

**Generated Summary:** _Laurie writes to her ex-boyfriend from high school. She wants to know if he is still at Enron. She also wants to meet up for lunch._

### Model Fine Tuning
We fine tuned and tested the four models. 
* We started with Decoder only models like GPT2, DistilGPT2, etc
* Though these models generated a subject line - they were innovative and did not seem to consider the email body
* On further reading and understanding , we started with BART and T5 models (encoder-decoder models)
* We could get good Rouge score with these two models 

The comparison of the Rouge score of each model is present in the below table

| Model  | Rouge 1 | Rouge 2 |  Rouge L  |
|----------|----------|----------|----------|
| BART    | 0.3006580658920587   | 0.15170335761446782   |0.2884998344468854   |
| T5 Small    | 0.27557781919299007   | 0.13223830150238886   |0.26705263028546283   |
| Distil GPT2    | 0.10658709214367193   | 0.041839523780108655   |0.10234448377437692   |
| GPT2    | 0.015072665203599737   | 0.005770499929776675   |0.013233120524232568   |

### Model Weights
We have saved all the model weights in Hugging Face Spaces.
* BART - https://huggingface.co/paramasivan27/bart_for_email_summarization_enron
* T5 small - https://huggingface.co/paramasivan27/t5small_for_email_summarization_enron
* Distill GPT2 - https://huggingface.co/paramasivan27/distilgpt2_for_email_summarization_enron
* GPT2 - https://huggingface.co/paramasivan27/gpt2_for_email_summarization_enron

### Observation and Further Reading

We have listed down the comparison between each model. This understanding made it clear to us on why BART and T5 modles performed better

|   |BART  | T5 Text-to-Text Transfer Transformer | GPT2-small |  DistilGPT  |
|----------|----------|----------|----------|----------|
| Developed By    | Facebook   | Google   |Open AI   | Open AI|
| Architecture    | • Combines bidirectional (like BERT) and autoregressive (like GPT) training objectives.<br/> • Encoder-decoder architecture, where the encoder is similar to BERT and the decoder is similar to GPT.   | • Encoder-decoder architecture. <br/> • Treats every NLP task as a text-to-text problem, converting inputs and outputs into text strings. | • Decoder only Autoregressive transformer architecture. | • Distilled version of GPT, created using a process called knowledge distillation. <br/> • Smaller and faster while retaining most of the performance of the original GPT model.|
| Training Objective    |• Pre-trained on a denoising autoencoder task, which involves corrupting text and then training the model to reconstruct the original text. <br/> • Supports a variety of noising functions,such as token masking, token deletion, and sentence permutation.  |• Pre-trained on a multi-task mixture of unsupervised and supervised tasks.<br/> • Uses a span-corruption objective during pre-training, where spans of text are masked and the model learns to predict the missing text.|• Trained to predict the next token in a sequence, given all the previous tokens in an unsupervised manner.|• Trained to mimic the behaviour of the larger GPT model by learning from its outputs.<br/> • Maintains the autoregressive language modelling objective.|
| Common Use Cases    |• Text generation <br/>• Text summarization <br/>• Machine translation <br/>• Question answering   |• Text generation <br/>• Text summarization <br/>• Machine translation <br/>• Question answering <br/>• Text classification   |• Text generation <br/>• Chatbots <br/>• Completion of text <br/>• Creative writing   |• Text generation <br/>• Chatbots <br/>• Applications requiring faster inference and reduced resource consumption.|

### Gradio App 
We tested the model weights loading and Rouge score calculation for three models BART, T5 Small and DistilGPT2 model. 
These notebooks loads the model from Hugging Face spaces and uses the Tests data to calculate Rouge score. These notebooks also contain a simple Colab Gradio App

| Model  | Colab Gradio App  |
|--------|-------------|
| BART  |  [Email_Subject_Line_BART_Gradio.ipynb](https://github.com/ch22group16/capstone-GenAI/blob/main/Email_Subject_Line_BART_Gradio.ipynb) |
| T5 Small | [Email_Subject_Line_T5Small_Gradio.ipynb](https://github.com/ch22group16/capstone-GenAI/blob/main/Email_Subject_Line_T5Small_Gradio.ipynb) |
| DistilGPT2 | [Email_Subject_Line_DistilGPT2_Gradio.ipynb](https://github.com/ch22group16/capstone-GenAI/blob/main/Email_Subject_Line_DistilGPT2_Gradio.ipynb) |

Finally, we have published the two models BART and T5 Gradio Spaces. The below table contains the name of the folder in this repository and the Hugging Face URL for the application 

| Model  | Repo Folder |  Gradio App  |
|--------|-------------|--------------|
| BART  | Email_Subject_Generation_BART | https://huggingface.co/spaces/paramasivan27/Email_Subject_Generation_BART |
| T5 Small | Email_Subject_Generation_T5Small |https://huggingface.co/spaces/paramasivan27/Email_Subject_Generation_T5Small |

### Human Validation
**Example 1: Conference Call**

![alt text](https://github.com/ch22group16/email_sub_generation/blob/main/HumanValidation/BART/ConferenceCall.JPG)
![alt text](https://github.com/ch22group16/email_sub_generation/blob/main/HumanValidation/T5Small/ConferenceCall.JPG)

**Example 2: Tickets**

![alt text](https://github.com/ch22group16/email_sub_generation/blob/main/HumanValidation/BART/DaveMatthews.JPG)
![alt text](https://github.com/ch22group16/email_sub_generation/blob/main/HumanValidation/T5Small/DaveMatthews.JPG)

**Example 3: Emmissions Testing**

![alt text](https://github.com/ch22group16/email_sub_generation/blob/main/HumanValidation/BART/EmmissionsTesting.JPG)
![alt text](https://github.com/ch22group16/email_sub_generation/blob/main/HumanValidation/T5Small/EmmissionsTesting.JPG)


## 2. Question Answering on AIML Queries

### Problem Description
This task involves fine-tuning a GPT variant model to answer questions specific to the AIML course, focusing on generating accurate and relevant answers.

### Dataset
We have used the dataset shared by the Talentspirit team below.

[dataset/Dataset-1-20240909T162549Z-001.zip](https://github.com/ch22group16/capstone-GenAI/blob/4f626e1b484a53f1ef99fa7176ea90d071f0b400/dataset/Dataset-1-20240909T162549Z-001.zip)

[dataset/Dataset-2-20240909T162549Z-001.zip](https://github.com/ch22group16/capstone-GenAI/blob/4f626e1b484a53f1ef99fa7176ea90d071f0b400/dataset/Dataset-2-20240909T162549Z-001.zip)

### Data preprocessing
The preprocessing in task 2 primarily involved in formatting the training dataset to an appropriate prompt format – we used 2 prompting formats GPT style and Alpaca style prompting.

**Train**  
![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Question_Answering_Training_and_Gradio_Noteboooks/qanda_dataset_visualization_train.png)
**Test**
![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Question_Answering_Training_and_Gradio_Noteboooks/qanda_dataset_visualization_test.png)

### Models
We have used the below models to train and test the data.

|   Model  | Training Notebook |
|----------|-------------------|
| GPT2 | [QnA_finetuning_gpt2_V4.ipynb](https://github.com/ch22group16/capstone-GenAI/blob/main/Question_Answering_Training_and_Gradio_Noteboooks/QnA_finetuning_gpt2_V4.ipynb)|
| Llama 2 | [Capstone_Group16_QnA_finetuning_LLAMA2_V1.ipynb](https://github.com/ch22group16/capstone-GenAI/blob/main/Question_Answering_Training_and_Gradio_Noteboooks/Capstone_Group16_QnA_finetuning_LLAMA2_V1.ipynb) |
| Gemma 2 | [QnA_gemma_2_2b_v5.ipynb](https://github.com/ch22group16/capstone-GenAI/blob/main/Question_Answering_Training_and_Gradio_Noteboooks/QnA_gemma_2_2b_v5.ipynb) |
| Llama 3 | [Capstone_Group16_QnA_finetuning_LLAMA3_V1.ipynb](https://github.com/ch22group16/capstone-GenAI/blob/main/Question_Answering_Training_and_Gradio_Noteboooks/Capstone_Group16_QnA_finetuning_LLAMA3_V1.ipynb) |

### Zero Shot Testing
1. Zero Shot testing in all the models
2. Hallucinations noticed before fine tuning
3. Focused on hyper parameters such as
  * Prompt structure
  * Max New Tokens / Max Length parameters

**Haluciniations:**

_What is Alexnet? 
Alexnet is a web application that allows you to create and manage your own websites. It is a web application that allows you to create and manage your own websites. It is a web application that allows you to create and manage your own websites

What is Neural Network? 
Neural networks are a type of neural network that is used to process information from a computer. They are used to process information from a computer and then process it back into a computer. Neural networks are used to process information from_

**Repetitive Answers:**

![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Human_Validation_Question_Answering/ZeroShotTesting.png)

### Model Fine Tuning
We fine tuned and tested the four models. 
* Though we initially tried encoder-decoder based models, we quickly pivoted to decoder-only / generative models to improve performance on unseen topics
* We started with finetuning GPT2
* Finetuned three more models Llama2, Gemma 2 and Llama 3.
* The training notebooks are as follows 

**Llama 2**  

![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Question_Answering_Training_and_Gradio_Noteboooks/Llama2_20_Epochs_training_loss.png)

**Gemma 2**  

![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Question_Answering_Training_and_Gradio_Noteboooks/Gemma2%2020%20Epochs_training_loss.png)

**Llama 3**  

![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Question_Answering_Training_and_Gradio_Noteboooks/Llama3_20_Epochs_training_loss.png)

### Model Weights

We have saved all the model weights in Hugging Face Spaces.
* GPT 2 - https://huggingface.co/paramasivan27/gpt2_for_q_and_a
* Llama 2 - https://huggingface.co/paramasivan27/Llama-2-7b-for_q_and_a
* Gemma 2 - https://huggingface.co/paramasivan27/Gemma_2b_it_q_and_a
* Llama 3 - https://huggingface.co/paramasivan27/llama-3-8b-bnb-4bit

The comparison of the Rouge score of each model of dataset-2 is present in the below table

| Model  | Rouge 1 | Rouge 2 |  Rouge L  |
|----------|----------|----------|----------|
| GPT2    | 0.36956118319733666   | 0.16392918775217533   |0.3127743307192723   |
| Llama 2    | 0.3912341324778206   | 0.18069427233839613   |0.3157717606974474   |
| Gemma 2    | 0.455100963377403  | 0.22904456388130273   |0.38447970761053407   |
| Llama 3    | 0.48342827227660445   | 0.2631626190945965   |0.41491957225471765   |

### Rouge Score Inference

**1.	Model Size and Capacity:**
*	Larger models like Llama 3 (8 billion parameters) and Gemma 2 (2 billion parameters) are more capable of capturing complex patterns in language and generalizing to topics not covered in training.
*	GPT-2 Small (124 million parameters) struggles significantly with generalization, leading to lower scores, especially on multi-word sequences (ROUGE-2) and sentence-level coherence (ROUGE-L).

**2.	Architecture Advancements:**
*	Llama 3 uses a more advanced transformer architecture with optimizations that allow it to generate more fluent and coherent responses, even when fine-tuned on relatively small datasets.
*	Gemma 2 benefits from a more modern architecture than GPT-2, though it doesn’t match Llama 3’s ability to maintain coherence across multiple domains.
*	Llama 2 performs well but doesn’t reach the same level of fine-tuning efficiency and generalization as Llama 3, which likely benefits from additional optimizations.

![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Human_Validation_Question_Answering/Model%20Comparison.png)

_Ref: [Sebastian Raschka, Post](https://www.linkedin.com/posts/sebastianraschka_an-often-asked-question-is-how-gpt-compares-activity-7243972293100511233-2QPa?utm_source=share&utm_medium=member_ios)_

**3.	Generalization to Unseen topic Questions:**
*	The ROUGE score differences can also be attributed to how well each model generalizes to topics not covered in the training data.
*	Llama 3 shows the best ability to generalize beyond the AI/ML domain, likely due to its large size, architectural sophistication, and fine-tuning efficiency.
*	Gemma 2 and Llama 2 also generalize well but not as effectively as Llama 3.
*	GPT-2 Small struggles the most with out-of-domain generalization, leading to significantly lower scores.
*	The following sample question is an interesting example, the training data does not contain anything related to RAG

![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Human_Validation_Question_Answering/Human_Validation_RAG.png)

### Observation and Further Reading
We have listed the comparisons between each model. 
|   |GPT2  | Gemma 2 | Llama 2 |  Llama 3  |
|----------|----------|----------|----------|----------|
| Developed By    | Open AI   | Google   |Meta   | Meta |
| Model Size    | 124 million   | 2 billion   | 7 billion   | 8 billion |
| Pre Trained Token Counts    | 10 Billion   |  2 Trillion  | 2 Trillion   | 10+ Trillion |
| Fine Tuning Token Counts    | 178 K   |  178 K  | 178 K   | 178 K |
| Architecture    | • GPT-2 is a unidirectional transformer. <br/> • It generates text by predicting the next token based on previous tokens, which can limit its understanding of bidirectional context. | • Text-to-text, decoder-only large language models. <br/> • Their relatively small size makes it possible to deploy them in environments with limited resources   |  • LLaMA (Large Language Model Meta AI) is a state-of-the-art transformer-based architecture optimized for downstream tasks.<br/> • It uses advanced techniques in multi-head attention and model scaling. |  • LLaMA 3 is an enhanced version of the LLaMA architecture, using cutting-edge techniques in transformer model training and efficient parameterization (bnb-4bit)  <br/>• It reduces resource consumption while maintaining performance. |
| Common Use Cases    |• Text generation <br/>• Text summarization <br/>• Machine translation <br/>• Question answering   |• Text generation tasks <br/> • question answering, •  summarization, and reasoning.   |• Text generation <br/>• Summarization <br/>• Transalation <br/>• Code generation   |• Text generation <br/>• Summarization <br/>• Transalation <br/>• Code generation|

### Gradio App

We tested the model weights loading and Rouge score calculation for four models GPT2, Gemma2, Llama 2, and Llama 3 model. 
These notebooks loads the model from Hugging Face spaces and uses the Tests data to calculate Rouge score. These notebooks also contain a simple Colab Gradio App

| Model  | Colab Gradio App  |
|--------|-------------|
| GPT2  |  [paramasivan27/AIML_QandA_finetuned_gpt2](https://huggingface.co/spaces/paramasivan27/AIML_QandA_finetuned_gpt2) |
| Llama 2 | [Llama2_Testing,_Rouge_Score_&_Gradio.ipynb](https://github.com/ch22group16/capstone-GenAI/blob/main/Question_Answering_Training_and_Gradio_Noteboooks/Llama2_Testing%2C_Rouge_Score_%26_Gradio.ipynb) |
| Gemma 2 | [Gemma2_Testing,_Rouge_Score_&_Gradio.ipynb](https://github.com/ch22group16/capstone-GenAI/blob/main/Question_Answering_Training_and_Gradio_Noteboooks/Gemma2_Testing%2C_Rouge_Score_%26_Gradio.ipynb) |
| Llama 3 | [Llama3_Testing,_Rouge_Score_&_Gradio.ipynb](https://github.com/ch22group16/capstone-GenAI/blob/main/Question_Answering_Training_and_Gradio_Noteboooks/Llama3_Testing%2C_Rouge_Score_%26_Gradio.ipynb) |

### Human Validation

**Example 1: EigenValues**

![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Human_Validation_Question_Answering/Human_Validation_GPT2_Eigen_Values.png)
![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Human_Validation_Question_Answering/Human_Validation_Gemma2_Eigen_Values.png)
![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Human_Validation_Question_Answering/Human_Validation_Llama3_Eigen_Values.png)

**Example 2: Backpropagation**

![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Human_Validation_Question_Answering/Human_Validation_GPT2_backpropagation.png)
![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Human_Validation_Question_Answering/Human_Validation_Gemma2_backpropagation.png)
![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Human_Validation_Question_Answering/Human_Validation_Llama3_Backpropagation.png)

**Example 2: Features**

![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Human_Validation_Question_Answering/Human_Validation_GPT2_features.png)
![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Human_Validation_Question_Answering/Human_Validation_Gemma2_features.png)
![alt text](https://github.com/ch22group16/capstone-GenAI/blob/main/Human_Validation_Question_Answering/Human_Validation_Llama3_features.png)
