# NovaVision Demo Package

Bu repo, `GNL - 03 Demo Package` Trello gorevi icin hazirlanmis basit bir NovaVision demo paketidir.

Paketin amaci gercek bir yapay zeka modeli calistirmak degil; NovaVision paket yapisini, executor mantigini, input/output tanimlarini ve `dependentDropdownlist` konfigurasyonunu gostermektir.

## Paket Ne Yapar?

Bu demo paketinde iki executor vardir:

- `SingleImageInfoExecutor`: 1 adet gorsel benzeri input alir ve 1 adet ozet output uretir.
- `ImageCompareExecutor`: 2 adet gorsel benzeri input alir ve 2 adet output uretir: karsilastirma ozeti ve benzerlik skoru.

Iki executor da konfigurasyon tarafinda `dependentDropdownlist` kullanir. Bu dropdown icinde iki secenek vardir:

- `BasicMode`: `textInput` ve `dropdownlist` alanlarini acar.
- `AdvancedMode`: `selectBox` ve `textInput` alanlarini acar.

## Trello Cevaplari

`Package Github Repo's = https://github.com/Abd2023/novavision_Demo_Package.git`

`What does your package do = Bu demo paket, iki adet gorsel isleme executor'u icerir. Ilk executor tek bir gorsel inputunu ozetler. Ikinci executor iki gorsel inputunu karsilastirir. Ayrica iki executor da dependent dropdown konfigurasyonunu gostermek icin hazirlanmistir.`

## Kontrol Listesi Karsiligi

- First executor: 1 input, 1 output.
- Second executor: 2 input, 2 output.
- Common feature: iki executor da `dependentDropdownlist` icerir.
- First option: 2 farkli field tipi acar: `textInput` ve `dropdownlist`.
- Second option: 2 farkli field tipi acar: `selectBox` ve `textInput`.

## Proje Yapisi

```text
apps/                 Ornek request payload dosyalari
notebooks/            Notebook dosyalari icin ayrilmis klasor
resources/            Ornek kaynak dosyalar icin ayrilmis klasor
src/executors/        Executor siniflari
src/models/           Pydantic PackageModel ve request/response modelleri
tests/                Trello kontrol listesini dogrulayan pytest testleri
service.py            Basit executor lookup ve bootstrap kontrol dosyasi
```

## Dogrulama

Asagidaki komutlar ile paketin temel yapisi dogrulanabilir:

```powershell
python -m pip install -r requirements.dev.txt
python -m pytest
python service.py
```

Beklenen sonuc:

- `python -m pytest`: tum testler basarili olur.
- `python service.py`: iki executor da `ready` olarak gorunur.

