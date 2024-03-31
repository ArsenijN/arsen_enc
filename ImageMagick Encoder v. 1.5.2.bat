@echo off
>NUL chcp 65001
setlocal enableextensions enabledelayedexpansion
for /f %%a in ('copy /Z "%~dpf0" nul') do set "CR=%%a"
for /f %%a in ('"prompt $H&for %%b in (0) do rem"') do set "BS=%%a"

::echo ^<ESC^>[92m [92mGreen[0m
type logo
@REM logo maked in https://patorjk.com/software/taag/#p=display&f=3D%20Diagonal&t=AIC
@REM IDK how to make "type" text: https://chat.openai.com/share/e369a9b8-938d-4909-95a4-111ae2993141
@REM echo ImageMagick converter v.1.5.1

@REM Colored text with powershell: https://stackoverflow.com/questions/2048509/how-to-echo-with-different-colors-in-the-windows-command-line
powershell write-host -fore Green ImageMagick converter v.1.5.2
powershell write-host -fore DarkGray -back Black 2023-2023. Open source. GitHub: https://github.com/ArsenijN/ImageMagick_Enc
echo Read config...
for /f "usebackq tokens=1,2 delims==\" %%a in ("config.txt") do (
    if "%%a" neq "" set "%%a=%%~b"
)

if "%formats%"=="" (
    set "formats=.jpg .jpeg .heic .webp .png .bmp .avif .jxl .jng .dng"
    echo Changing formats to default.
    echo Please, change settings in config.txt^^!
    2>NUL >NUL timeout -t 3
)

::Before 1.5.5:
set Parameters=%ParametersWoConvert%

if "%Language%"=="Ukr" set /p quality=Введіть налаштування якості 0..100 (примітка: для lossless форматів буде встановлено значення 100): 
if "%Language%"=="En" set /p quality=Enter a quality setting of 0..100 (note: lossless formats will be set to 100): 

if "%Language%"=="Ukr" echo Створення папок...
if "%Language%"=="En" echo Making folders...

for /F "usebackq tokens=1-3 delims=/. " %%a in (`wmic os get LocalDateTime^,LocalDateTime /value ^| findstr "="`) do (
  set "datetime=%%a%%b%%c"
)
if "%Language%"=="Ukr" echo Значення змінної datetime: %datetime%
if "%Language%"=="En" echo Datetime variable value: %datetime%

if exist "converted" (
    2>NUL mkdir "converted\.old\%datetime%"
    for %%F in ("converted\*.*") do (
        2>NUL >NUL move "%%F" "converted\.old\%datetime%\"
    )
)
if exist "originals" (
    @REM 2>NUL >NUL mkdir "originals\.old\%datetime%"
    @REM for %%F in ("originals\*.*") do (
    @REM     2>NUL >NUL move "originals\%%F" "originals\.old\%datetime%\"
    @REM )
    @REM for %%F in ("originals\%sameformats%") do (
    @REM     2>NUL >NUL move "originals\*%formats%" "originals\.old\%datetime%\"
    @REM )
    2>NUL mkdir "originals\.old\%datetime%"
    for %%F in ("originals\*.*") do (
        2>NUL >NUL move "%%F" "originals\.old\%datetime%\"
    )
)

2>NUL mkdir converted
>nul 2>NUL mkdir originals
set ImageCount=1

if "%Language%"=="Ukr" echo Конвертація...
if "%Language%"=="En" echo Converting...

@REM setlocal enabledelayedexpansion
REM Ваша змінна з розширеннями
@REM set "extensions=.jpg .png .avif"
REM Розділити значення за допомогою пробілів
for %%i in (%formats%) do (
    set "sameformats=!sameformats! *%%i"
)
REM Вивести результат
@REM echo Результат: %new_extensions%
@REM echo Результат: %sameformats%
@REM endlocal

@REM set "sameformats=*.jpg *.jpeg *.heic *.webp *.png *.bmp *.avif *.jxl *.jng *.dng"
@REM PDF doesn`t supported with unk error

for %%F in (%formats%) do (
    set "format=%%F"
    set "files=0"
    for %%x in (*%%F) do @(set /a files+=1 >nul)
    setlocal enabledelayedexpansion
    for %%x in (*%%F) do (
        set "ImageCount=0"
        set "Difference=0"
        @REM Напевно, ChatGPT невірно зрозумів для чого наступна команда:
        @REM for /F %%G in ('dir /a:-d /s /b "converted\*%format%" ^| find /c ":"') do set /a "ImageCount=%%G"
        @REM По факту це призначено для виключення наступних папок для підрахунку, а не вибору тільки однієї
        @REM for /F %%G in ('dir /a:-d /s /b "converted\*%format%" ^| find /c ":"') do set /a "ImageCount=%%G"
        for /F %%G in ('dir /a:-d /s /b "converted" ^| findstr /v /c:"converted\.old\" ^| findstr /v /c:"converted\\.old\\" ^| find /c ":"') do set ImageCount=%%G
        set /a "Difference=ImageCount"
        
        if "%%~dpa"=="%cd%\" (
            if "%Language%"=="Ukr" (
                echo Процесс конвертації %%F: !Difference!/!files!
            )
            if "%Language%"=="En" (
                echo Converting %%F files: !Difference!/!files!
            )
        )
        
        REM Тут вставте загальну логіку конвертації для різних форматів
        for %%a in (%sameformats%) do (
            if "%%~dpa"=="%cd%\" (
                REM Ваша логіка конвертації тут
                @REM if not "%Parameters%"=="" (
                @REM     2>NUL >NUL move "%%a" "originals\"
                @REM ) else (
                if "%TOACimg%"=="1" (
                    for %%a in (%sameformats%) do (
                        for /f "delims=" %%b in ('ImageMagick\identify -format "%%[channels]" %%a') do set IdentifyAlpha=%%b
                        @REM echo %IdentifyAlpha%
                        if not "!IdentifyAlpha:%substring%=!"=="%IdentifyAlpha%" (
                            echo Image may contains Alpha channel. Moving in converted... ^(%substring%^)
                            2>NUL >NUL move "%%a" "originals\"
                            @REM %substring% doesn't have a value from batch file, maybe a multithreading problem?
                        ) else (
                            echo Image doesn't have Alpha channel. Converting... ^(%substring%.^)
                            ImageMagick\convert !Parameters! -quality !quality! "%%a" "converted\%%~na%outformat%"
                            2>NUL >NUL move "%%a" "originals\"
                        )
                    )
                    @REM echo %IdentifyAlpha%
                    @REM if "%IdentifyAlpha%"=="srgba" move "%%a" "originals\"
                    @REM if "%IdentifyAlpha%"=="rgba" ImageMagick\convert !ParametersWoConvert! -quality !quality! "%%a" "converted\%%~na%outformat%"
                ) else (
                    ImageMagick\convert !Parameters! -quality !quality! "%%a" "converted\%%~na%outformat%"
                    2>NUL >NUL move "%%a" "originals\"
                )
                @REM echo kk
                @REM )
                @REM echo %quality%
            )
        )
        REM Використовуйте змінні !format! та !ImageCount!
        for /F %%G in ('dir /a:-d /s /b "converted\*%format%" ^| find /c ":"') do set /a "ImageCount=%%G"
    )
    if "%Language%"=="Ukr" (
        echo:
        echo Було конвертовано файлів %%F: !Difference!/!files!
    )
    if "%Language%"=="En" (
        echo:
        echo Converted %%F files: !Difference!/!files!
    )
    endlocal
)

if exist "%temp_folder%" rmdir /S /Q "%temp_folder%"
endlocal



@REM setlocal enabledelayedexpansion
@REM for %%a in ("*.png*") do (
@REM     for /F %%G in ('dir /a:-d /s /b "converted" ^| findstr /v /c:"converted\.old\" ^| findstr /v /c:"converted\\.old\\" ^| find /c ":"') do set ImageCount=%%G
@REM     set /a Difference=ImageCount - jpgfiles - jpegfiles - heicfiles - webpfiles
@REM     if "%Language%"=="Ukr" <nul set /p"=!BS!!CR!Процесс конвертації png: !Difference!/!pngfiles!"
@REM     if "%Language%"=="En" <nul set /p"=!BS!!CR!Png conversion process: !Difference!/!pngfiles!"
@REM     ImageMagick\magick -quality !quality! "%%a" "converted\%%~na.avif"
@REM     >NUL move "%%a" "originals\%%a"
@REM )
@REM if "%Language%"=="Ukr" <nul set /p"=!BS!!CR!Процесс конвертації png: !Difference!/!pngfiles!"
@REM if "%Language%"=="En" <nul set /p"=!BS!!CR!Png conversion process: !Difference!/!pngfiles!"
@REM echo:
@REM if "%Language%"=="Ukr" echo Було конвертовано файлів png: %Difference%/%pngfiles%
@REM if "%Language%"=="En" echo Converted png files: %Difference%/%pngfiles%
@REM endlocal


set convertedfiles=0 & for %%a in (converted/*.*) do set /a convertedfiles+=1
if "%Language%"=="Ukr" (
echo Конвертування закінчено!
echo Було конвертовано %convertedfiles% файлів.
)
if "%Language%"=="En" (
echo Conversion complete!
echo %convertedfiles% files have been converted.
)


@REM if "%Language%"=="Ukr" pause
@REM if "%Language%"=="En" pause


pause

::Comment: it may be works
::154..168 delete
::145..149 delete
::127..129 delete
::116..124 delete
::104..110 delete
::102 delete
::For delete: ^^
::It doesn't move a original files in originals folder. Hmm...

::From config.txt:
::autoCompressionQuality="1"
::Auto quality function for different formats (this will work as a nice loss for a smaller file size for now)
::How works; coefficients - jpg=1, avif=0.44, webp=0.63, etc. These coefficients should be selected with minimal loss of image quality, and for this a difference test should be performed. For a future feature.
::Cool idea, but takes time.
::encoding="1"
::0 - decode
::1 - encode
::Or use "Type of out format"
::Not in this version
::Mostly - this is a combination of a separate decoding file
::Decoder cannot decode image whose name is more than ~128 characters, solution: rename file before decoding, return name later. Possible injuries? Yes, change the name before encoding and revert (but I don't plan to do that yet, sorry)
::My title that didn't work when decoding: friendly-smiling-successful-man-in-black-suit-waving-hand-hello-gesture-introduce-himself-saying-hi-welcome-and-greet-someone-white-background_176420-45255.avif
::Info: You can add your own values here, but leave only language and pngQuality, otherwise you won't have text (silent mode) and/or png compression working.
::Please, add decoding into encoder!
::Please, add new features!
