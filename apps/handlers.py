
import asyncio
from aiogram import Bot, Dispatcher,types
from bot_token import BOT_TOKEN
from aiogram.types import Message
from aiogram.filters import CommandStart,StateFilter
from aiogram import F,Router
from db import add_chat,add_message,add_user,check
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from main import Bot as bot
router = Router()

class Form(StatesGroup):
    waiting_for_name = State()

#Обработчик команды /start
@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    if check(message.from_user.id,message.chat.id)==False:
        await state.set_state(Form.waiting_for_name)
        await message.answer("Привет! Как вас зовут? Пожалуйста, напишите ваше имя и фамилию.")
    else:await message.answer("Уже зарегистрированы!")


#Обработчик, который занимается сообщениями после команды /start, добавляет пользователя в бд с его именем и фамилией
@router.message(StateFilter(Form.waiting_for_name))
async def handle_name(message: Message, state: FSMContext):
    user_id = message.from_user.id
    full_name = message.text.split()
    
    
    if len(full_name) == 2:
        name, lastname = full_name
        add_chat(message.chat.id)
        add_user(user_id, name, lastname,message.chat.id)  # Добавление пользователя в базу данных
        await message.answer(f"Спасибо! Ваше имя и фамилия: {name} {lastname}")
        await state.clear()
    else:
        await message.answer("Пожалуйста, введите имя и фамилию в формате 'Имя Фамилия'.")
    

#Обработчик всех текстовых сообщений, работает если только пользователь ещё не вводил команду start
@router.message(F.content_type == types.ContentType.TEXT)
async def handle_text(message: types.Message, state: FSMContext):
    user_id=message.from_user.id
    if check(user_id,message.chat.id)==False:
        await message.answer("Я не понимаю. Пожалуйста, начните с команды /start.")
    else:
        await message.answer(f"Сообщение {message.text} сохранено!")
        add_message(user_id,message.chat.id,message.text)

# Обработчик для фото-сообщений
@router.message(F.content_type == types.ContentType.PHOTO)
async def handle_photo(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
   
    file_id = message.photo[-1].file_id  
    media_url = await message.bot.get_file(file_id)  # Получаем файл с Telegram
    media_url = f'https://api.telegram.org/file/bot{BOT_TOKEN}/{media_url.file_path}'
    
    await message.answer(f"Сообщение фото сохранено!")
    add_message(user_id, chat_id, "Фото", media_type="photo", media_url=media_url, file_id=file_id)

# Обработчик для видео-сообщений
@router.message(F.content_type == types.ContentType.VIDEO)
async def handle_video(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    
    file_id = message.video.file_id
    media_url = await message.bot.get_file(file_id)
    media_url = f'https://api.telegram.org/file/bot{BOT_TOKEN}/{media_url.file_path}'

    await message.answer(f"Сообщение видео сохранено!")
    add_message(user_id, chat_id, "Видео", media_type="video", media_url=media_url, file_id=file_id)


# Обработчик для аудио-сообщений
@router.message(F.content_type == types.ContentType.AUDIO)
async def handle_audio(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    
    file_id = message.audio.file_id
    media_url = await message.bot.get_file(file_id)
    media_url = f'https://api.telegram.org/file/bot{BOT_TOKEN}/{media_url.file_path}'
    
    await message.answer(f"Сообщение аудио сохранено!")
    add_message(user_id, chat_id, "Аудио", media_type="audio", media_url=media_url, file_id=file_id)



