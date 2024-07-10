# 1. 기본
## 사용 예시
**Markdown**

```md
![header](https://capsule-render.vercel.app/api?)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api? />
```

# 2. 모양 `type=`

1. `wave`(default)
2. `egg`
3. `shark`
4. `slice`
5. `rect`
6. `soft`
7. `rounded`
8. `cylinder`
9. `waving`
10. `venom`
11. `transparent`

## 사용예시

**Markdown**

```md
![header](https://capsule-render.vercel.app/api?type=wave)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave />
```


# 배경 색상 `color=`

### `auto`: 자동 색상 무작위 변경


**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=auto)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=auto />
```

## `timeAuto`: 시간에 따라 무작위 색상 변경

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=timeAuto)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=timeAuto />
```
## `random`: 무작위 색상

**MarkDown**

 ```md
![header](https://capsule-render.vercel.app/api?type=wave&color=random)
```
  
**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=random />
```

## `gradient`: 그라데이션

  **MarkDown**

  ```md
  ![header](https://capsule-render.vercel.app/api?type=wave&color=gradient)
  ```
  
  **HTML**

  ```html
  <img src="https://capsule-render.vercel.app/api?type=wave&color=gradient />
  ```

## `timeGradient`: 시간에 따라 그라데이션

  **MarkDown**

  ```md
  ![header](https://capsule-render.vercel.app/api?type=wave&color=timeGradient)
  ```
  
  **HTML**

  ```html
  <img src="https://capsule-render.vercel.app/api?type=wave&color=timeGradient />
  ```
## `_hexcode`: 기본값(#B897FF)

  **MarkDown**

  ```md
  ![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF)
  ```
  
  **HTML**

  ```html
  <img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF />
  ```

## `_custom_gradient`: 사용자 정의 그라데이션

  **MarkDown**

  ```md
  ![header](https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8)
  ```
  
  **HTML**

  ```html
  <img src="https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8 />
  ```

# 부분(섹션) `section=`
- 배경 위치

## `header`: 상단(기본)

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8&section=header)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8&section=header />
```

## `footer`: 하단

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8&section=footer)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8&section=footer />
```


# 높이 `height=`
- default 120

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8&section=footer&height=100)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8&section=footer&height=100 />
```

# 텍스트 `text=`
- 제목 글

## `%20`: 공백

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘%20셋)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘%20셋 />
```

## `-nl-`: 줄바꿈

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋 />
```

# 설명(줄 추가) `desc=`

* 특수문자 사용 불가
* 일반적으로 공백(%20)만 사용함

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글 />
```

# 텍스트 애니메이션 `animation=`

## `fadeIn`: 페이드인 1.2초

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=fadeIn)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=fadeIn />
```

## `scaleIn`: 날라옴 0.8초

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=scaleIn)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=scaleIn />
```

## `blink`: 깜박임 0.6초

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=blink)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=blink />
```

## `blinking`: 깜박임 1.6초

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=blinking)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=blinking />
```

## `twinkling`: 반짝임 4초

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=twinkling)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=twinkling />
```


# 제목 글자 색상 `fontColor=`
- 값은 "#"없이 16진수 코드여야 함
- 텍스트쿼리 뒤에 쓰기
## 사용 예시

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000 />
```




# 제목 글자 크기 `fontSize=`
- default = 70
- 텍스트 쿼리 뒤에 쓰기

## 사용 예시
**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000&fontSize=50)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000&fontSize=50 />
```

# 제목 글자 위치 조정

## x축 조정 `fontAlign=`
- default 50

## 사용 예시

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000&fontSize=50&fontAlign=20)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000&fontSize=50&fontAlign=20 />
```

## y축 조정 `fontAlignY=`
- default 50

## 사용예시
**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000&fontSize=50&fontAlignY=20)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000&fontSize=50&fontAlignY=20 />
```

# 설명 글자 크기 `descSize=`
- default = 20
- desc쿼리 뒤에 쓰기

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50 />
```

# 설명 위치 조정

## x축 조정 `descAlign=`
- default 50

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50&descAlign=30)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50&descAlign=30 />
```

## y축 조정 `descAlignY=`
- default 50

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50&descAlignY=30)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50&descAlignY=30 />
```

# 회전 `rotate=`
- -360 ~ 0
- 0 ~ 360

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50&descAlignY=30&rotate=60)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50&descAlignY=30&rotate=60 />
```

# 글자 외곽 색상 변경 `stroke=`
- #이 없는 16진수 색상코드

## 사용예시

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&fontColor=1111&text=글%20자&stroke=888845)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&fontColor=1111&text=글%20자&stroke=888845 />
```


# 글자 외곽 색상 폭 `strokeWidth=`
- stroke 쿼리 뒤에 쓰기

## 사용 예시

**MarkDown**

```md
![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&fontColor=1111&text=글%20자&stroke=888845&strokeWidth=3)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&fontColor=1111&text=글%20자&stroke=888845&strokeWidth=3 />
```