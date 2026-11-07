# 글꼴 라이선스

이 저장소의 `fonts/*.woff2`와, 빌드가 장표(`refs/*.html`)에 잘라 넣은 글꼴은 모두 **SIL Open Font License 1.1** 글꼴의 수정본(글자를 줄인 것)입니다. 라이선스 전문은 [`OFL.txt`](OFL.txt)에 있습니다.

- 원본은 `scripts/fetch_fonts.py`가 [google/fonts](https://github.com/google/fonts)의 `ofl/` 디렉터리에서 받습니다(원본 ttf는 저장소 밖).
- 줄인 글꼴에도 이름표 0(저작권) · 13(라이선스) · 14(라이선스 주소)를 남기고, 장표 HTML의 글꼴 앞에는 사람이 읽는 고지 주석을 붙입니다(OFL 조건 2).
- 저작권 문구에 **예약 이름**(Reserved Font Name)이 있고 그것이 글꼴 이름에 들어 있으면, 수정본의 글꼴 이름에서 `DRG`로 바꿉니다(OFL 조건 3). 장표 CSS에서 부르는 이름은 그대로입니다.
- 나눔 글꼴 일부는 파일 안 라이선스 칸에 `NHN Corporation`만 적혀 있지만, google/fonts에서 `OFL.txt`와 함께 OFL로 배포되는 파일입니다.
- 이 표는 `python3 scripts/fontlic.py`로 파일 안 정보를 읽어 만듭니다. 손으로 고치지 마세요.

| 글꼴(파일 이름) | 굵기 | 저작권 (파일 안 표기) | 예약 이름 | 파일 안 라이선스 표기 |
|---|---|---|---|---|
| Archivo | 500 · 700 · 800 · 900 | Copyright 2020 The Archivo Project Authors (https://github.com/Omnibus-Type/Archivo) | — | SIL OFL 1.1 |
| BarlowCondensed | 500 · 700 | Copyright 2017 The Barlow Project Authors (https://github.com/jpt/barlow) | — | SIL OFL 1.1 |
| BlackHanSans | 400 | Copyright 2015 The Black Han Sans Project Authors (https://github.com/zesstype/Black-Han-Sans) | — | SIL OFL 1.1 |
| DoHyeon | 400 | Copyright 2018 The Do Hyeon Project Authors | — | SIL OFL 1.1 |
| DotGothic16 | 400 | Copyright 2020 The DotGothic16 Project Authors (https://github.com/fontworks-fonts/DotGothic16/) | — | SIL OFL 1.1 |
| Fredoka | 500 · 600 · 700 | Copyright 2016 The Fredoka Project Authors (https://github.com/hafontia/Fredoka-One) | — | SIL OFL 1.1 |
| Gaegu | 700 | Copyright 2018 The Gaegu Project Authors | — | SIL OFL 1.1 |
| Galmuri11 | 400 · 700 | Copyright (c) 2019-2025 Lee Minseo (quiple@quiple.dev) | — | SIL OFL 1.1 |
| GothicA1 | 300 · 400 · 500 · 600 · 700 · 800 · 900 | (C) Copyright HanYang I&C Co.,Ltd. All rights reserved. | — | SIL OFL 1.1 |
| GowunBatang | 400 · 700 | Copyright 2021 The Gowun Batang Project Authors (https://github.com/yangheeryu/Gowun-Batang) | — | SIL OFL 1.1 |
| GowunDodum | 400 | Copyright 2021 The Gowun Dodum Project Authors (https://github.com/yangheeryu/Gowun-Dodum) | — | SIL OFL 1.1 |
| Hahmlet | 400 · 500 · 600 · 700 · 800 | Copyright 2020 The Hahmlet Project Authors (https://github.com/hyper-type/hahmlet) | — | SIL OFL 1.1 |
| IBMPlexMono | 400 · 500 · 600 · 700 | Copyright 2017 IBM Corp. All rights reserved. | — | SIL OFL 1.1 |
| IBMPlexSansKR | 300 · 400 · 500 · 600 · 700 | Copyright 2018 IBM Corp. All rights reserved. | — | SIL OFL 1.1 |
| JetBrainsMono | 400 · 500 · 600 · 700 | Copyright 2020 The JetBrains Mono Project Authors (https://github.com/JetBrains/JetBrainsMono) | — | SIL OFL 1.1 |
| Jua | 400 | Copyright 2018 The BM JUA Project Authors | — | SIL OFL 1.1 |
| MartianMono | 400 · 600 · 800 | Copyright 2020 The Martian Mono Project Authors (https://github.com/evilmartians/mono) | — | SIL OFL 1.1 |
| NanumBrushScript | 400 | Copyright © 2010 NHN Corporation. All rights reserved. Font designed by Sandoll Communications Inc. | — | NHN Corporation → OFL (google/fonts `ofl/`) |
| NanumGothic | 400 · 700 · 800 | Copyright © 2011 NHN Corporation. All rights reserved. Font designed by Sandoll Communications Inc. | — | NHN Corporation → OFL (google/fonts `ofl/`) |
| NanumGothicCoding | 400 · 700 | Copyright © 2009 NHN Corporation. All rights reserved. Font designed by Sandoll Communications Inc. | — | SIL OFL 1.1 |
| NanumMyeongjo | 400 · 700 · 800 | Copyright © 2010 NHN Corporation. All rights reserved. Font designed by FONTRIX. | — | NHN Corporation → OFL (google/fonts `ofl/`) |
| NanumPenScript | 400 | Copyright © 2010 NHN Corporation. All rights reserved. Font designed by Sandoll Communications Inc. | — | SIL OFL 1.1 |
| NotoSansKR | 400 · 500 · 600 · 700 · 900 | (c) 2014-2021 Adobe (http://www.adobe.com/), with Reserved Font Name 'Source'. | Source | SIL OFL 1.1 |
| NotoSerifKR | 200 · 300 · 500 · 600 · 700 · 800 · 900 | (c) 2017-2024 Adobe (http://www.adobe.com/). | — | SIL OFL 1.1 |
| Orbit | 400 | Copyright 2022 The Orbit Project Authors (https://github.com/JAMO-TYPEFACE/Orbit) | — | SIL OFL 1.1 |
| RedHatMono | 500 · 600 | Copyright 2024 The Red Hat Project Authors (https://github.com/RedHatOfficial/RedHatFont) | — | SIL OFL 1.1 |
| SairaCondensed | 500 · 700 · 800 | Copyright 2016 The Saira Project Authors (omnibus.type@gmail.com), with reserved font name "Saira". | Saira | SIL OFL 1.1 |
| SairaSemiCondensed | 500 · 600 · 700 | Copyright 2016 The Saira Project Authors (omnibus.type@gmail.com), with reserved font name "Saira". | Saira | SIL OFL 1.1 |
| SplineSansMono | 500 | Copyright 2022 The Spline Sans Mono Project Authors (https://github.com/SorkinType/SplineSansMono) | — | SIL OFL 1.1 |
| Sunflower | 500 · 700 | Copyright 2008 The Sunflower Project Authors | — | SIL OFL 1.1 |
