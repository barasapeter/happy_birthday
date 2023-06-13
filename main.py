import customtkinter as ctk
from PIL import Image

phone = ctk.CTk()
phone.wm_attributes('-topmost', True)
phone.overrideredirect(True)
phone.geometry('320x650')

count = 0
start_x = 0
start_y = 0

def start_drag(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y

def drag(event):
    delta_x = event.x - start_x
    delta_y = event.y - start_y
    x = phone.winfo_x() + delta_x
    y = phone.winfo_y() + delta_y
    phone.geometry(f"+{x}+{y}")

def launch_scan_widgets():
    home_scan_button.pack_forget()
    menu_bar.pack_forget()
    congrats_text.pack(padx=5, pady=5, fill='x')
    emojis.pack(fill='both', expand='yes')
    claim_button.pack(pady=10, side='bottom')

def back_home():
    claim_button.pack_forget()
    nav_button.pack_forget(),
    main_frame.pack_forget()
    new_present.pack_forget()
    emojis.pack_forget()
    congrats_text.pack_forget()
    menu_bar.pack(side='top', fill='x')
    main_frame.pack(fill='both', expand='yes')
    home_scan_button.pack(expand='yes')
    nav_button.pack(pady=1, side='bottom')

def switch_presents():
    global count, new_present
    emojis.pack_forget()
    presents = ['me', 'cake', 'skill', 'doodle']; count += 1
    presents_dictionary = dict(zip([i[0] for i in enumerate(presents, start=1)], 
                                   [i[1] for i in enumerate(presents, start=1)])) 
    
    if count != 1:
        previous_present = eval(presents_dictionary[count - 1])
    else:
        previous_present = eval(presents[0])
    
    if count > len(presents):
        count = 1
        previous_present = eval(presents[-1])
    new_present = eval(presents_dictionary[count])
    previous_present.pack_forget()
    new_present.pack(expand='yes', fill='both')
    try:
        dynamic_text.set(f'CLAIM {presents[count+1]}')
    except IndexError:
        dynamic_text.set('CLAIM ice cake')

status_bar = ctk.CTkFrame(phone, corner_radius=0)
status_bar.pack(fill='x')

menu_bar = ctk.CTkFrame(phone, corner_radius=0)
menu_bar.pack(fill='x', side='top')

main_frame = ctk.CTkFrame(phone, corner_radius=0)
main_frame.pack(fill='both', expand='yes')

status_bar.bind("<ButtonPress-1>", start_drag)
status_bar.bind("<B1-Motion>", drag)

ctk.CTkButton(status_bar, text=None, 
              width=10, height=10, fg_color='#FF5F57', 
              hover_color='#FF5F56', command=phone.destroy).pack(padx=(5, 0), side='left')

ctk.CTkButton(status_bar, text=None, 
              width=10, height=10, fg_color='#FEBC2E', 
              hover_color='#FEBC2E', command=phone.destroy).pack(padx=(2, 0), side='left')

ctk.CTkButton(status_bar, text=None, 
              width=10, height=10, fg_color='#2AC840', 
              hover_color='#2AC840', command=phone.destroy).pack(padx=(2, 5), side='left')

ctk.CTkLabel(status_bar, text=None, 
             image=ctk.CTkImage(Image.open('./icons/bardisplay.png'), 
                                size=(110, 20))).pack(side='right')

ctk.CTkButton(menu_bar, text=None, hover_color='#F05F1B', fg_color='transparent', corner_radius=0, width=20,
              image=ctk.CTkImage(Image.open('./icons/cake.png'), 
                                 size=(300, 200))).pack(side='top', padx=5, pady=5)
ctk.CTkLabel(menu_bar, font=ctk.CTkFont('Consolas', 24, 'bold'), text='Hey Peter,\nit\'s your birthday!', text_color='#F05F1B').pack()

home_scan_button = ctk.CTkButton(main_frame, text='View your presents', fg_color='#F07122', hover_color='#F05F1B',
                                 font=ctk.CTkFont('Consolas', 18, 'bold'), width=200, height=40, command=launch_scan_widgets)
home_scan_button.pack(expand='yes')

congrats_text = ctk.CTkButton(main_frame, font=ctk.CTkFont('Consolas', 20, 'bold'), fg_color='transparent',
                             text=None, text_color='#B33722', corner_radius=0, command=switch_presents,
                             image=ctk.CTkImage(Image.open('./icons/hbd2.png'), size=(300, 160)), compound='top', hover_color='#FFB733')

me = ctk.CTkLabel(main_frame, text=None, 
             image=ctk.CTkImage(Image.open('./icons/me.png'), 
                                size=(115, 380)))
emojis = ctk.CTkLabel(main_frame, text=None, 
             image=ctk.CTkImage(Image.open('./icons/emojis.png'), 
                                size=(300, 250)))

cake = ctk.CTkLabel(main_frame, text=None, 
             image=ctk.CTkImage(Image.open('./icons/cake.png'), 
                                size=(400, 300)))

skill = ctk.CTkLabel(main_frame, text=None, 
             image=ctk.CTkImage(Image.open('./icons/skill.png'), 
                                size=(300, 310)))

doodle = ctk.CTkLabel(main_frame, text=None, 
             image=ctk.CTkImage(Image.open('./icons/birthday.png'), 
                                size=(300, 300)))

dynamic_text = ctk.StringVar()
dynamic_text.set('CLAIM VIBES')

claim_button = ctk.CTkButton(main_frame, textvariable=dynamic_text, fg_color='transparent', hover_color='#FFB733', corner_radius=40, 
                            border_width=3, border_color='#F15A1C', text_color='black', font=ctk.CTkFont('Consolas', 18, 'bold'))

nav_button = ctk.CTkButton(main_frame, text=None, width=100,
              hover_color='grey', fg_color='#999999',
              corner_radius=100, height=10,
              command=back_home)

nav_button.pack(pady=1, side='bottom')

phone.mainloop()
