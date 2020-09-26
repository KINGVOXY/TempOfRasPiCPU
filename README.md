# RaspberryPi CPU温度記録
RaspberryPiのCPU温度を1分おきにlog/temp_log.csvに記録します。

temp_log.csvファイルは以下の内容になります。
```csv
年-月-日,時-分,温度(℃)
```
使用方法は次の通りです。

# 使用の流れ
## 1. 任意のディレクトリに置いた後、main.py14行目log/temp_log.csvのパスを変更
main.pyの14行目を
```py
with open('[main.pyがあるディレクトリの絶対パス]/log/temp_log.csv', 'a') as f:
```
に変更する。

## 2. pythonのパスを確認
ターミナルで
```sh
which python3
```
を実行。

## 3. logCPUTemp.serviceを編集
logCPUTemp.serviceのExecStartを、
```
ExecStart=[pythonのパス] [main.pyのパス]
```
に変更。

## 4. serviceファイルをコピー
ターミナルで
```sh
sudo cp logCPUTemp.service /etc/systemd/system/
```
を実行。

## 5. systemctlで自動起動
ターミナルで
```sh
sudo systemctl enable logCPUTemp.service
sudo systemctl start logCPUTemp.service
```
を実行