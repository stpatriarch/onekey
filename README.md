## OneKey

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<br>

### 🔐 Օֆլայն գաղտնաբառերի գեներատոր՝ SHA-256 հիման վրա։

Այս գործիքը իրենից ներկացանում է այս [հռչակագրի](https://github.com/stpatriarch/decmans/blob/main/manifests/onekey_manifest.txt) ռեալիզացիան: Այն օգտագործում է **SHA-256** հեշավորման ալգորիթմը, դեկոդավորելով այն և **BASE-64** կոդավորումով, գեներացնելու համար ապահով, չկրկնվող գաղտաբառեր, առանց դրանք հիշելու կամ պահպանելու անհրաժեշտության։

**Տեադրման և շահագործման գործընթացը** [ասյտեղ](docs/INSTALL_ARM.md)

#### 🚨 Խնդիրը

* Մարդիկ օգտագործում են տասնյակ հաշիվներ։
* Յուրաքանչյուրի համար պահանջվում է եզակի և բարդ գաղտնաբառ։
* Բոլոր գաղտնաբառերը հիշելն անհնար է → օգտվողները կրկնում են թույլ գաղտնաբառերը։
* Օնլայն գաղտնաբառերի մենեջերները բազմիցս ենթարկվել են հաքերական հարձակումների → հարյուր հազարավոր հաշիվներ վտանգի տակ են հայտնվել։

---

#### 💡 Լուծումը

* Գործիքը աշխատում է **օֆլայն**՝ բացառելով երրորդ անձանց միջամտությունը։

* Օգտագործվում է **մեկ բանալի**, որը կարելի է պահպանել․

  * **ֆիզիկական կրիչի վրա**,
  * **QR-կոդում**,
  * **NFC պիտակում**։

* Բանալին պարզապես **SHA հեշ է**, օրինակ․

```sh

ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
```

* Նույնիսկ եթե այն հայտնվի ուրիշի ձեռքում, **իրենից ոչ մի ինֆորմացիա չի ներկացանում**, թե ինչ է և որտեղ է կիրառելի։

---

#### ⚙️ Ինչպես է աշխատում

1. Մուտքագրեք բանալին։
2. Մուտքագրեք հոսթը (օր. `instagram`, `facebook`)։
3. (Օպցիոնալ) — կամ էլ հոսթի փոխարեն նշեք օգտանուն։
4. Ալգորիթմը կիրառում է **SHA-256 եռակի հեշավորում** և գեներացնում ունիկալ գաղտնաբառ։

#### 📌 Գաղտնաբառի օրինակ

```sh

7V1QRtxY2WRtBG01ESgz4UMG49oUca6lnvhQFEFzPGA=
KxgvhkGvQPng1MTISNkf2dN8S0iyP/Tle7EjDBNvGkk=
```

#### 🛡️ Անվտանգություն

* Գաղտնաբառերը ապահովում են **288.4 բիթ էնտրոպիա**։
* Կռահելը համարվում է **մաթեմատիկապես անհնարին** (միլիարդավոր տարիներ՝ հարյուրավոր սուպերհամակարգիչների համար)։
* Գաղտնաբառը ոչ պահելու, ոչ էլ հիշելու կարիք չկա։

---

## 🇷🇺

### 🔐 Генератор офлайн-паролей на основе SHA-256

Этот инструмент представляет собой реализацию данного [манифеста](https://github.com/stpatriarch/decmans/blob/main/manifests/onekey_manifest.txt)
Он использует алгоритм хеширования SHA-256, декодирует его и при помощи BASE-64 кодирования генерирует надёжные, неповторяющиеся пароли, без необходимости их запоминать или хранить.

**Процесс устновки и пользования** [здесь](docs/INSTALL_RU.md)

#### 🚨 Проблема

* У каждого человека десятки аккаунтов.
* Для каждого нужен уникальный и сложный пароль.
* Запомнить все пароли невозможно → пользователи используют слабые и повторяющиеся комбинации.
* Онлайн-менеджеры паролей неоднократно подвергались взломам → сотни тысяч учётных записей оказались под угрозой.

#### 💡 Решение

* Инструмент работает **офлайн** — исключено вмешательство третьих лиц.
* Используется **один ключ**, который можно хранить:

  * на **физическом носителе**;
  * в **QR-коде**;
  * в **NFC-метке**.
* Ключ — это просто **SHA-хеш**, например:

  ```sh

  ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
  ```

* Даже если он попадёт в чужие руки, **он не несёт информации**, где и как используется.

#### ⚙️ Как работает

1. Введите ключ.
2. Введите хост (например: `instagram`, `facebook`).
3. (Опционально) — укажите имя пользователя вместо хоста.
4. Алгоритм применяет **SHA-256 тройное хеширование** и выдаёт уникальный пароль.

#### 📌 Пример результата

```sh

7V1QRtxY2WRtBG01ESgz4UMG49oUca6lnvhQFEFzPGA=
KxgvhkGvQPng1MTISNkf2dN8S0iyP/Tle7EjDBNvGkk=
```

#### 🛡️ Безопасность

* Пароли обладают **288,4 битами энтропии**.
* Подбор считается **математически невозможным** (миллиарды лет для сотен суперкомпьютеров).
* Пароль не нужно хранить и не нужно запоминать.

---

## 🇬🇧

### 🔐 Offline Password Generator based on SHA-256

This tool is an implementation of this [manifest](https://github.com/stpatriarch/decmans/blob/main/manifests/onekey_manifest.txt). It uses the SHA-256 hashing algorithm, decodes it with BASE-64 encoding generates secure, non-repeating passwords without the need to memorize or store them.

**Process of install and use** [here](docs/INSTALL_EN.md)

#### 🚨 Problem

* People use dozens of accounts.
* Each requires a unique and strong password.
* Remembering them all is impossible → users reuse weak passwords.
* Online password managers have been hacked multiple times → hundreds of thousands of accounts were exposed.

#### 💡 Solution

* The tool works **offline**, eliminating third-party interference.
* It uses **a single key**, which can be stored:

  * on a **physical medium**;
  * in a **QR code**;
  * in an **NFC tag**.
* The key is just a **SHA hash**, for example:

  ```sh

  ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
  ```

* Even if it falls into someone else’s hands, **it reveals nothing** about what it is or where it is used.

#### ⚙️ How it works

1. Enter your key.
2. Enter the host (e.g., `instagram`, `facebook`).
3. (Optional) — enter your username.
4. The algorithm applies **SHA-256 triple hashing** and generates a unique password.

#### 📌 Example output

```sh

7V1QRtxY2WRtBG01ESgz4UMG49oUca6lnvhQFEFzPGA=
KxgvhkGvQPng1MTISNkf2dN8S0iyP/Tle7EjDBNvGkk=
```

#### 🛡️ Security

* Passwords provide **288.4 bits of entropy**.
* Brute-forcing them is **mathematically infeasible** (billions of years for hundreds of supercomputers).
* No need to store or remember the password.
