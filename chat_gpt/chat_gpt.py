import os
import base64
import aspose.words as aw
import openai
import string
import random
import time
import json
import requests
from io import BytesIO
from lumaai import AsyncLumaAI

from aiogram import F, Router
from aiogram.types import BufferedInputFile, Message, CallbackQuery, URLInputFile, FSInputFile
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.enums.parse_mode import ParseMode
from .config import OPENAI_API_KEY
from supa import BOT
from concurrent.futures import ThreadPoolExecutor
from asyncio.events import get_running_loop


from db.db import neuro, asks_update, role, user_tokens_update, premium_tokens_update, update_ai, set_mode, ans_gpt, ready_answer_gpt, lingo, user_tokens
from db.db_premium import check_user_prem
from db.luma import check_user_in_luma, times_killer, take_mode_kling, take_seconds
from db.udio import times_udio_killer, check_user_in_udio

from ikb.ikb import photo_again_ru, photo_again_eng, photo_again_es, photo_again_cn, tokens_ikb_ru, tokens_ikb_eng, tokens_ikb_es, tokens_ikb_ru_prem, tokens_ikb_eng_prem, tokens_ikb_es_prem, tokens_ikb_cn_prem, tokens_ikb_cn, choose_luma_ikb_eng_pro, choose_luma_ikb_eng_standard, choose_luma_ikb_es_standard, choose_luma_ikb_es_pro, choose_luma_ikb_cn_standard, choose_luma_ikb_cn_pro, choose_luma_ikb_ru_pro, choose_luma_ikb_ru_standard, with_no_photo, choose_udio_ikb_ru, choose_udio_ikb_eng, choose_udio_ikb_es, choose_udio_ikb_cn

bot = BOT

class Conditions(StatesGroup):
    text_for_luma = State()
    photo_for_luma = State()
    udio_text = State()

kling_prompt: dict[int, dict[str]] = {}


router = Router()

client_1 = openai.AsyncOpenAI(
    api_key="sk-lf7iHfVz4WTHyarmAB8R71Vr1IsfBf7X",
    base_url="https://api.proxyapi.ru/openai/v1"
)

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer sk-BkRAIS0V63H49gtvyUGumjeZ8dUhr7m7icwM4XoIVwqXltIFzVIFBsnb020v'
    }


@router.callback_query(F.data == "gen_video")
async def luma(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    username = callback.from_user.username
    video_pro = FSInputFile("C:\\Users\\user\\Desktop\\projects\\local\\AI-Bot\\chat_gpt\\kling_PRO.mp4", filename="kling_PRO.mp4")
    video_standard = FSInputFile("C:\\Users\\user\\Desktop\\projects\\local\\AI-Bot\\chat_gpt\\kling_STANDARD.mp4", filename="kling_STANDARD.mp4")
    if username not in ["CODE_PIZZA", "Kseny_7"]:
        if check_user_in_luma(uid) == False:
            if lingo(uid) == "RU":
                    await callback.message.answer_video(
                        video=video_pro,
                        caption="👑<b>Kling Pro</b>\n\n🗓Срок подписки: <b>7 дней</b>\n\nДоступные тарифы👇",
                        parse_mode=ParseMode.HTML,
                        reply_markup=choose_luma_ikb_ru_pro()
                    )
                    await callback.message.answer_video(
                        video=video_standard,
                        caption="🚀<b>Kling Standard</b>\n\n🗓Срок подписки: <b>7 дней</b>\n\nДоступные тарифы👇",
                        parse_mode=ParseMode.HTML,
                        reply_markup=choose_luma_ikb_ru_standard()
                    )
            if lingo(uid) == "ENG":
                    await callback.message.answer_video(
                        media=video_pro,
                        caption="<b>Kling Pro</b>\n\n🗓Subscription period: <b>7 days</b>\n\nAvailable tariffs👇",
                        parse_mode=ParseMode.HTML,
                        reply_markup=choose_luma_ikb_eng_pro()
                    )
                    await callback.message.answer_video(
                        media=video_standard,
                        caption="<b>Kling Standard</b>\n\n🗓Subscription period: <b>7 days</b>\n\nAvailable tariffs👇",
                        parse_mode=ParseMode.HTML,
                        reply_markup=choose_luma_ikb_eng_standard()
                    )
            if lingo(uid) == "ES":
                    await callback.message.answer_video(
                        media=video_pro,
                        caption="<b>Kling Pro</b>\n\n🗓Periodo de suscripción: <b>7 días</b>\n\nTarifas disponibles👇",
                        parse_mode=ParseMode.HTML,
                        reply_markup=choose_luma_ikb_es_pro()
                    )
                    await callback.message.answer_video(
                        media=video_standard,
                        caption="<b>Kling Standard</b>\n\n🗓Periodo de suscripción: <b>7 días</b>\n\nTarifas disponibles👇",
                        parse_mode=ParseMode.HTML,
                        reply_markup=choose_luma_ikb_es_standard()
                    )
            if lingo(uid) == "CN":
                    await callback.message.answer_video(
                        media=video_pro,
                        caption="<b>Kling Pro</b>\n\n🗓订阅期限：<b>7 天</b>\n\n 可用关税👇",
                        parse_mode=ParseMode.HTML,
                        reply_markup=choose_luma_ikb_cn_pro()
                    )
                    await callback.message.answer_video(
                        media=video_standard,
                        caption="<b>Kling Standard</b>\n\n🗓订阅期限：<b>7 天</b>\n\n 可用关税👇",
                        parse_mode=ParseMode.HTML,
                        reply_markup=choose_luma_ikb_cn_standard()
                    )
        else:
            if lingo(uid) == "RU":
                await callback.message.answer(
                    "Подробно опишите то что хотите увидеть в вашем видео"
                )
                await state.set_state(Conditions.text_for_luma)
            elif lingo(uid) == "ENG":
                await callback.message.answer(
                    "Describe in detail what you would like to see in the video"
                )
                await state.set_state(Conditions.text_for_luma)
            elif lingo(uid) == "ES":
                await callback.message.answer(
                    "Describa detalladamente lo que quiere ver en su vídeo"
                )
                await state.set_state(Conditions.text_for_luma)
            elif lingo(uid) == "CN":
                await callback.message.answer(
                    "详细描述您希望在视频中看到的内容"
                )
                await state.set_state(Conditions.text_for_luma)
    else:
        await callback.message.answer(
            "Подробно опишите то что хотите увидеть в вашем видео"
        )
        await state.set_state(Conditions.text_for_luma)

@router.message(StateFilter(Conditions.text_for_luma), F.text)
async def photo_for_luma(message: Message, state: FSMContext):
    uid = message.from_user.id
    await state.update_data(prompt = message.text)
    kling_prompt[message.from_user.id] = await state.get_data()
    if lingo(uid) == "RU":
        await message.answer(
            "Отправьте фото, которое хотите оживить.\n\nЕсли хотите продолжить без фото, нажмите на кнопку ниже",
            reply_markup=with_no_photo()
        )
    if lingo(uid) == "ENG":
        await message.answer(
            "Send the photo you want to animate.\n\nIf you want to continue without a photo, click the button below",
            reply_markup=with_no_photo()
        )
    if lingo(uid) == "ES":
        await message.answer(
            "Envía la foto que quieres animar.\n\nSi quieres continuar sin foto, haz clic en el botón de abajo",
            reply_markup=with_no_photo()
        )
    if lingo(uid) == "CN":
        await message.answer(
            "发送要制作动画的照片\n\n如果您想在没有照片的情况下继续，请点击下面的按钮",
            reply_markup=with_no_photo()
        )
    await state.set_state(Conditions.photo_for_luma)

def check_status_kling(url_res, res):
    while json.loads(res.text)["status"] != "success":
        res = requests.get(url_res, headers=headers)

async def async_check_status_kling(loop, url_res, res):
    with ThreadPoolExecutor() as executor:
        await loop.run_in_executor(executor, check_status_kling, url_res, res)


@router.callback_query(F.data == "no_photo")
async def just_video(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "⌛️"
    )
    loop = get_running_loop()
    uid = callback.from_user.id

    url_endpoit = "https://api.gen-api.ru/api/v1/networks/kling"
    url_endpoit = "https://api.gen-api.ru/api/v1/networks/kling"
    input = {
    "translate_input": True,
    "prompt": kling_prompt[callback.from_user.id]["prompt"],
    "model": f"{take_mode_kling(uid)}",
    "duration": f"{take_seconds(uid)}",
    "ratio": "16:9"
}
    
    generation = requests.post(url_endpoit, json=input, headers=headers)
    id = json.loads(generation.text)["request_id"]

    url_res = f"https://api.gen-api.ru/api/v1/request/get/{id}"
    time.sleep(10)
    pre_res = requests.get(url_res, headers=headers)
    await async_check_status_kling(loop, url_res, pre_res)
    res = requests.get(url_res, headers=headers)
    video_link = json.loads(res.text)["result"][0]
    video_from_url = URLInputFile(video_link)
    await callback.message.answer_video(
        video=video_from_url,
        caption="📹📹📹"
    )
    times_killer(uid)
    await state.set_state(default_state)

@router.message(StateFilter(Conditions.photo_for_luma), F.photo)
async def img_to_mp4(message: Message, state: FSMContext):
    uid = message.from_user.id
    loop = get_running_loop()
    photo_object = message.photo[-1]
    photo_id = "".join(random.choices(string.ascii_letters + string.digits, k = 5))

    url_upload = "https://api.imgbb.com/1/upload"
    url_endpoit = "https://api.gen-api.ru/api/v1/networks/kling"

    await message.bot.download(file=photo_object, destination=f"/home/nick/Nick_Gpt/{photo_id}.jpeg")
    with open(f"/home/nick/Nick_Gpt/{photo_id}.jpeg", "rb") as file:
        payload = {
            "key": "d67765069757eb5ab9ff5dfdfb888279",
            "image": base64.b64encode(file.read())
        }

        res = requests.post(url_upload, data=payload)
        photo = json.loads(res.text)["data"]["url"]
    await message.answer(
        "⌛️"
    )

    input = {
    "translate_input": True,
    "image": photo,
    "prompt": kling_prompt[message.from_user.id]["prompt"],
    "model": f"{take_mode_kling(uid)}",
    "duration": f"{take_seconds(uid)}",
    "ratio": "16:9"
}
    
    generation = requests.post(url_endpoit, json=input, headers=headers)
    id = json.loads(generation.text)["request_id"]
    print(id)

    url_res = f"https://api.gen-api.ru/api/v1/request/get/{id}"

    time.sleep(10)
    pre_res = requests.get(url_res, headers=headers)
    await async_check_status_kling(loop, url_res, pre_res)
    res = requests.get(url_res, headers=headers)
    video_link = json.loads(res.text)["result"][0]
    video_from_url = URLInputFile(video_link)
    await message.answer_video(
        video=video_from_url,
        caption="📹📹📹"
    )
    times_killer(uid)
    os.remove(f"/home/nick/Nick_Gpt/{photo_id}.jpeg")
    await state.set_state(default_state)

@router.callback_query(F.data == "gen_music")
async def start_music(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    username = callback.from_user.username
    if username not in ["CODE_PIZZA", "Kseny_7"]:
        if check_user_in_udio(uid) == False:
            if lingo(uid) == "RU":
                await callback.message.answer(
                    text="🎧<b>Udio</b>\n\n🗓Срок подписки: <b>7 дней</b>\n\nДоступные тарифы👇",
                    parse_mode=ParseMode.HTML,
                    reply_markup=choose_udio_ikb_ru()
                )
            elif lingo(uid) == "ENG":
                await callback.message.answer(
                    text="🎧<b>Udio</b>\n\n🗓Subscription period: <b>7 days</b>\n\nAvailable tariffs👇",
                    parse_mode=ParseMode.HTML,
                    reply_markup=choose_udio_ikb_eng()
                )
            elif lingo(uid) == "ES":
                await callback.message.answer(
                    text="🎧<b>Udio</b>\n\n🗓Periodo de suscripción: <b>7 días</b>\n\nTarifas disponibles👇",
                    parse_mode=ParseMode.HTML,
                    reply_markup=choose_udio_ikb_es()
                )
            elif lingo(uid) == "CN":
                await callback.message.answer(
                    text="🎧<b>Udio</b>\n\n🗓订阅期限：<b>7 天</b>\n\n 可用关税👇",
                    parse_mode=ParseMode.HTML,
                    reply_markup=choose_udio_ikb_cn()
                )
        else:
            if lingo(uid) == "RU":
                await callback.message.answer(
                    "Подробно опишите то что вы хотите услышать в аудио"
                )
            elif lingo(uid) == "ENG":
                await callback.message.answer(
                    "Describe in detail what you want to hear in the audio"
                )
            elif lingo(uid) == "ES":
                await callback.message.answer(
                    "Describa detalladamente lo que desea escuchar en el audio"
                )
            elif lingo(uid) == "CN":
                await callback.message.answer(
                    "详细描述您希望在音频中听到的内容"
                )
    else:         
        if lingo(uid) == "RU":
            await callback.message.answer(
                "Подробно опишите то что вы хотите услышать в аудио"
            )
        elif lingo(uid) == "ENG":
            await callback.message.answer(
                "Describe in detail what you want to hear in the audio"
            )
        elif lingo(uid) == "ES":
            await callback.message.answer(
                "Describa detalladamente lo que desea escuchar en el audio"
            )
        elif lingo(uid) == "CN":
            await callback.message.answer(
                "详细描述您希望在音频中听到的内容"
            )
    await state.set_state(Conditions.udio_text)

@router.message(StateFilter(Conditions.udio_text), F.text)
async def make_music(message: Message, state: FSMContext):
    uid = message.from_user.id
    loop = get_running_loop()
    await message.answer(
        "⌛️"
    )

    url_endpoit = "https://api.gen-api.ru/api/v1/networks/udio"

    input = {
    "translate_input": True,
    "prompt": message.text,
    "lyrics_type": "generate",
    "prompt_strength": 0.5,
    "lyrics_strength": 0.5,
    "generation_quality": 0.75,
    "model_type": "udio130-v1.5",
    "bypass_prompt_optimization": False,
    "lyrics_placement_start": 0.2,
    "lyrics_placement_end": 0.9,
    "clarity_strength": 0.25,
    "mode": "regular"
    }

    generation = requests.post(url_endpoit, json=input, headers=headers)
    pre_id = json.loads(generation.text)
    id = json.loads(generation.text)["request_id"]
    print(id)
    print(pre_id)

    url_res = f"https://api.gen-api.ru/api/v1/request/get/{id}"

    time.sleep(10)
    pre_res = requests.get(url_res, headers=headers)
    await async_check_status_kling(loop, url_res, pre_res)
    res = requests.get(url_res, headers=headers)
    audio_link = json.loads(res.text)["result"][0]
    audio_from_url = URLInputFile(audio_link)
    await message.answer_audio(
        audio=audio_from_url,
        caption="🎧🎧🎧"
    )
    times_udio_killer(uid)


@router.message(F.text)
async def fin_answer(message: Message):
    message_gpt = message.text
    uid = message.from_user.id
    if user_tokens(uid) > 0:
        await message.answer(
            "⌛️"
        )
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
                os.remove(f"/home/nick/Nick_Gpt/{new_name}.docx")
                set_mode(uid, "1")
        else:
            if neuro(uid) in ["gpt-3.5-turbo", "gpt-4o-mini", " o1-preview", "o1-mini"]:
                await message.answer(
                    answer
                )
            else:
                if lingo(uid) == "RU":
                    await message.answer_photo(photo=answer, reply_markup=photo_again_ru())
                elif lingo(uid) == "ENG":
                    await message.answer_photo(photo=answer, reply_markup=photo_again_eng())
                elif lingo(uid) == "ES":
                    await message.answer_photo(photo=answer, reply_markup=photo_again_es())
                elif lingo(uid) == "CN":
                    await message.answer_photo(photo=answer, reply_markup=photo_again_cn())
        if check_user_prem(uid == True):
                if neuro(uid) in ["gpt-3.5-turbo", "gpt-4o-mini", " o1-preview", "o1-mini"]:
                    premium_tokens_update(uid, total_tokens)
                else:
                    premium_tokens_update(uid, 1000)
                    update_ai(uid, "gpt-4o-mini")
        else:
                if neuro(uid) in ["gpt-3.5-turbo", "gpt-4o-mini", " o1-preview", "o1-mini"]:
                    user_tokens_update(uid, total_tokens)
                else:
                    user_tokens_update(uid, 1000)
                    update_ai(uid, "gpt-4o-mini")
    else:
        if check_user_prem(uid) == False:
            if lingo(uid) == "RU":
                message.answer(
                    f"Закончились токены! на данный момент ваш баланс {user_tokens(uid)}. Вы можете пополнить баланс выбрав нужный для вас тариф!",
                    reply_markup=tokens_ikb_ru()
                )
            elif lingo(uid) == "ENG":
                message.answer(
                    f"We're out of tokens! As of this moment, your balance {user_tokens(uid)}. You can refill your balance by choosing the tariff you need!",
                    reply_markup=tokens_ikb_eng()
                )
            elif lingo(uid) == "ES":
                message.answer(
                    f"Nos hemos quedado sin fichas. Tu saldo actual es de {user_tokens(uid)}. Puedes recargar tu saldo eligiendo la tarifa que necesites.",
                    reply_markup=tokens_ikb_es()
                )
            elif lingo(uid) == "CN":
                message.answer(
                    f"我們沒有代幣了! 您的餘額目前是 {user_tokens(uid)}. 您可以選擇所需的電價來充值您的餘額!",
                    reply_markup=tokens_ikb_cn()
                )
        else:
            if lingo(uid) == "RU":
                message.answer(
                    f"Закончились токены! на данный момент ваш бланас {user_tokens(uid)}. Вы можете пополнить баланс выбрав нужный для вас тариф!",
                    reply_markup=tokens_ikb_ru_prem()
                )
            elif lingo(uid) == "ENG":
                message.answer(
                    f"We're out of tokens! As of this moment, your balance {user_tokens(uid)}. You can refill your balance by choosing the tariff you need!",
                    reply_markup=tokens_ikb_eng_prem()
                )
            elif lingo(uid) == "ES":
                message.answer(
                    f"Nos hemos quedado sin fichas. Tu saldo actual es de {user_tokens(uid)}. Puedes recargar tu saldo eligiendo la tarifa que necesites",
                    reply_markup=tokens_ikb_es_prem()
                )
            elif lingo(uid) == "CN":
                message.answer(
                    f"我們沒有代幣了! 您的餘額目前是 {user_tokens(uid)}. 您可以選擇所需的電價來充值您的餘額!",
                    reply_markup=tokens_ikb_cn_prem()
                )