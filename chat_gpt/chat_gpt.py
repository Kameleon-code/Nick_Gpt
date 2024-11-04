import os
import aspose.words as aw
import openai
from io import BytesIO

from aiogram import F, Router
from aiogram.types import BufferedInputFile, Message
from .config import OPENAI_API_KEY
from supa import BOT


from db.db import neuro, asks_update, role, user_tokens_update, premium_tokens_update, update_ai, set_mode, ans_gpt, ready_answer_gpt, lingo, user_tokens
from db.db_premium import check_user_prem, user_in_prem, days_update_plus

from ikb.ikb import photo_again_ru, photo_again_eng, photo_again_es, photo_again_cn, tokens_ikb_ru, tokens_ikb_eng, tokens_ikb_es, tokens_ikb_ru_prem, tokens_ikb_eng_prem, tokens_ikb_es_prem, tokens_ikb_cn_prem, tokens_ikb_cn

bot = BOT


router = Router()

client_1 = openai.AsyncOpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://api.proxyapi.ru/openai/v1",
)

@router.message(F.text)
async def fin_answer(message: Message):
    message_gpt = message.text
    uid = message.from_user.id
    if user_tokens(uid) < 0:
        if check_user_prem(uid) == False:
            if lingo(uid) == "RU":
                await message.answer(
                    "❗️Закончились токены\n\n👇Выберите нужный тариф",
                    reply_markup=tokens_ikb_ru()
                )
            if lingo(uid) == "ENG":
                await message.answer(
                    "❗️Out of tokens\n\n👇Select the desired tariff",
                    reply_markup=tokens_ikb_eng()
                )
            if lingo(uid) == "ES":
                await message.answer(
                    "❗️Sin fichas\n\n👇Selecciona la tarifa deseada",
                    reply_markup=tokens_ikb_es()
                )
            if lingo(uid) == "CN":
                await message.answer(
                    "❗️代币用完\n\n👇选择所需的费率",
                    reply_markup=tokens_ikb_cn()
                )
        elif check_user_prem(uid) == True:
            if lingo(uid) == "RU":
                await message.answer(
                    "❗️Закончились токены\n\n👇Выберите нужный тариф",
                    reply_markup=tokens_ikb_ru_prem()
                )
            if lingo(uid) == "ENG":
                await message.answer(
                    "❗️Out of tokens\n\n👇Select the desired tariff",
                    reply_markup=tokens_ikb_eng_prem()
                )
            if lingo(uid) == "ES":
                await message.answer(
                    "❗️Sin fichas\n\n👇Selecciona la tarifa deseada",
                    reply_markup=tokens_ikb_es_prem()
                )
            if lingo(uid) == "CN":
                await message.answer(
                    "❗️代币用完\n\n👇选择所需的费率",
                    reply_markup=tokens_ikb_cn_prem()
                )
    else:
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        if neuro(uid) in ["gpt-3.5-turbo", "gpt-4o-mini"]:
                asks_update(uid)
                if check_user_prem(uid) == True:
                    if role(uid) == "1":
                        prompt = "You clever man, expert of any topic"
                    elif role(uid) == "2":
                        prompt = f"You are an expert essay writer. Please write a well-structured and comprehensive essay on the following topic:**Topic:** {message_gpt}**Essay Requirements:**- **Length:** {5000}.- **Structure:** Include an introduction, {8} body paragraphs, and a conclusion.- **Style:** philosophical, historical-biographical, journalistic, literary-critical, popular science, fiction character.- **Formatting:** Use clear and coherent paragraphs with topic sentences.- **Content Guidelines:**- **Introduction:** Introduce the topic, provide background information, and state a clear thesis statement.- **Body Paragraphs:** Each paragraph should focus on a single main idea that supports the thesis. Provide evidence, examples, and explanations.- **Paragraph 1:** {message_gpt}- **Paragraph 2:** {message_gpt}- **(Add more paragraphs as needed)**- **Conclusion:** Summarize the key points discussed, restate the thesis in light of the evidence presented, and provide a closing thought or call to action.**Additional Instructions:**- Ensure the essay is original and free of plagiarism.- Use proper grammar, punctuation, and spelling.- Incorporate relevant quotes or references where appropriate, and cite sources if necessary.- Avoid using first-person pronouns unless specified otherwise.- Maintain objectivity and present multiple viewpoints if relevant to the topic.```**Instructions to Use the Template:**1. **Replace Placeholders:**- `{message_gpt}`: Enter the specific topic or question your essay should address.- `{message_gpt}`: Specify the approximate word count you want for the essay.- `{1000}`: Indicate how many body paragraphs the essay should contain (e.g., 3).- `{3}`, `{6}`, etc.: Provide the main points or aspects you want each body paragraph to cover."
                    elif role(uid) == "3":
                        prompt = f"You are an expert coursework writer. Please write course work for {5000} number of words. Write a well-structured and comprehensive essay on the following topic:**Coursework Paper Template**---**Title: {message_gpt}****Abstract:**- A brief summary {2000} words of the main points of the paper, the research problem: number of words, methodology, and conclusions.---**Introduction:**- Introduce the topic of your coursework.- Provide background information to contextualize the topic for {2000} number of words.- State a clear thesis statement that identifies the central argument or purpose of the paper. Write Introduction for {2000} number of words---**Body Paragraphs:**- **Paragraph 1: {message_gpt}**- Present the first main idea that supports the thesis for {2000} number of words.- Provide evidence, examples, or data to back up the argument for {2000} number of words.- Include explanations and analysis of the evidence provided. Number of words in Paragraph 1: {2000} - **Paragraph 2: {message_gpt}**- Focus on a second main idea relevant to the thesis.- Support this idea with additional evidence, case studies, or scholarly references.- Analyze the significance of this point in relation to the overall argument. Write Paragraph 2 for {2000} Number of words - **Paragraph 3: {message_gpt}**- Discuss a third main idea that further bolsters the thesis.- Cite relevant literature or statistical data to validate the argument.- Explain how this idea connects with previous paragraphs. Write Paragraph 3 for {2000} Number of words- **Paragraph 4: {message_gpt}**- Introduce a contrasting viewpoint or counter-argument.- Provide evidence that brings depth to this discussion.- Discuss how this perspective either supports or challenges your thesis. Write Paragraph 4 for {2000} Number of words - **Paragraph 5: {message_gpt}**- Explore a related aspect of the topic that enhances the argument.- Use examples from academic literature or case studies.- Draw connections to the overall argument of the paper. Write Paragraph 5 for {2000} Number of words- **Paragraph 6: {message_gpt}**- Present any concluding thoughts on the main ideas discussed.- Discuss potential implications of the research findings.- Suggest areas for further research or study.---**Conclusion:**- Summarize the key points discussed throughout the paper.- Restate the thesis in light of the evidence presented.- Provide final thoughts or a call to action regarding the topic.---**References:**- Include a list of all sources cited in your paper in a properly formatted bibliography (e.g., APA, MLA, Chicago).---**Formatting Guidelines:**- Ensure proper grammar, punctuation, and spelling throughout the paper.- Use clear and coherent paragraphs with topic sentences.- Maintain objectivity, and present multiple viewpoints if relevant to the topic.- Follow any specific formatting requirements (font size, margins, etc.) as outlined by your instructor.---**Instructions for Use:**1. **Replace Placeholders:**- {message_gpt}: Enter the title of your coursework.- {message_gpt}, {message_gpt}, etc.: Specify the key points or themes each body paragraph will cover.2. **Customize Content:**- Adapt the content to fit your specific topic and research findings.3. **Proofread:**- Review the final document for clarity, coherence, and adherence to academic standards.By following this template, you can create a well-structured coursework paper that effectively communicates your research and arguments Write Paragraph 6 for {2000} Number of words"
                    elif role(uid) == "4":
                        prompt = f"Hello, ChatGPT! Today, you are acting as an SEO expert with many years of experience! Please write an SEO article on the topic f'{message_gpt}' that includes the following elements:1. **Keywords**: Use the keywords '{message_gpt}', '{message_gpt}', and '{message_gpt}' naturally in the text, ensuring that each line with a keyword is optimized.2. **Article Structure**: Break the text into logical sections with headings (H1, H2, H3) and include a brief introduction, main body, and conclusion.3. **Optimization**: Ensure the article contains a meta description that is appealing and informative.4. **Internal and External Links**: Include links to related internal and external resources to improve SEO optimization.5. **Formatting**: Use lists, bold, and italic text to highlight key points and make the text easier to read.6. **Readability**: Write the article in a way that is understandable and interesting for the reader, avoiding complicated technical terms without explanation.7. **Length**: Make the article approximately {6000} words long."
                else:
                    prompt = "You clever man, expert of any topic"
                chat_completion = await client_1.chat.completions.create(
                    messages=[
                        {"role": "user", "content": message_gpt}, {"role": "system", "content": prompt, "max_tokens": 8000}], model=neuro(uid)
                                )
                total_tokens = chat_completion.usage.total_tokens
                answer = chat_completion.choices[0].message.content
                if check_user_prem(uid) == True:
                    premium_tokens_update(uid, total_tokens)
                else:
                    user_tokens_update(uid, total_tokens)
                if role(uid) in ["2", "3", "4"]:
                        punctuation = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
                        new_name = message_gpt
                        for i in message_gpt:
                            if i in punctuation:
                                new_name = new_name.replace(i, '')
                        builder.writeln(answer)
                        doc.save(f"{new_name}.docx")
                        with open(f"{new_name}.docx", "rb") as file:
                            file_for_send = BufferedInputFile(
                                file.read(),
                                filename=f"{new_name}.docx"
                            )      
                            await message.reply_document(file_for_send, caption=f"Вот ваша работа на тему: '{message.text}'")
                        os.remove(f"C:\\Users\\user\\Desktop\\projets from kitty\\AI-Bot\\{new_name}.docx")
                        set_mode(uid, "1")
                else:
                    await message.answer(
                        answer
                        )
        elif neuro(uid) == "o1-mini" or neuro(uid) == "o1-preview":
                    chat_completion = await client_1.chat.completions.create(
                    model=neuro(uid),
                    messages=[
                        {
                            "role": "user", 
                            "content": message_gpt
                        }
                    ]
                )      
                    total_tokens = chat_completion.usage.total_tokens
                    answer = chat_completion.choices[0].message.content
                    if check_user_prem(uid) == True:
                        premium_tokens_update(uid, total_tokens)
                    else:
                        user_tokens_update(uid, total_tokens)
                    if role(uid) in ["2", "3", "4"]:
                            punctuation = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
                            new_name = message_gpt
                            for i in message_gpt:
                                if i in punctuation:
                                    new_name = new_name.replace(i, '')
                            builder.writeln(answer)
                            doc.save(f"{new_name}.docx")
                            with open(f"{new_name}.docx", "rb") as file:
                                file_for_send = BufferedInputFile(
                                    file.read(),
                                    filename=f"{new_name}.docx"
                                )      
                                await message.reply_document(file_for_send, caption=f"Вот ваша работа на тему: '{message.text}'")
                            os.remove(f"C:\\Users\\user\\Desktop\\projets from kitty\\AI-Bot\\{new_name}.docx")
                            set_mode(uid, "1")
                    else:
                        await message.answer(
                            answer
                            )
        elif neuro(uid) in ["DALL-E 3"]:
                image = await client_1.images.generate(
                      model="dall-e-3",
                      prompt=message_gpt,
                      size="1024x1024",
                      quality="hd",
                      n=1,
                      style="vivid"
               )
                answer = image.data[0].url
                total_tokens = 1000
                if check_user_prem(uid) == True:
                    premium_tokens_update(uid, total_tokens)
                else:
                    user_tokens_update(uid, total_tokens)
                if lingo(uid) == "RU":
                    await message.answer_photo(photo=answer, reply_markup=photo_again_ru())
                elif lingo(uid) == "ENG":
                    await message.answer_photo(photo=answer, reply_markup=photo_again_eng())
                elif lingo(uid) == "ES":
                    await message.answer_photo(photo=answer, reply_markup=photo_again_es())
                elif lingo(uid) == "CN":
                    await message.answer_photo(photo=answer, reply_markup=photo_again_cn())
                update_ai(uid, "gpt-4o-mini")
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        if role(uid) in ["2", "3", "4"]:
                punctuation = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
                new_name = message_gpt
                for i in message_gpt:
                    if i in punctuation:
                        new_name = new_name.replace(i, '')
                builder.writeln(answer)
                doc.save(f"{new_name}.docx")
                with open(f"{new_name}.docx", "rb") as file:
                    file_for_send = BufferedInputFile(
                        file.read(),
                        filename=f"{new_name}.docx"
                    )      
                    await message.reply_document(file_for_send, caption=f"Вот ваша работа на тему: '{message.text}'")
                os.remove(f"C:\\Users\\user\\Desktop\\projets from kitty\\AI-Bot\\{new_name}.docx")
                set_mode(uid, "1")