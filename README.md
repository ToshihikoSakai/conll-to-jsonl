# conll-to-jsonl
CoNLL形式からJSONL形式へ変更してくれます。

# Usage

```bash
python CoNLLtoJSONL.py > output.jsonl
```

# File Format
## CoNLL形式ファイル
```bash
東京	LOCATION
は	O
今日も	TIME
晴れ	O
```

## JSONL形式ファイル
```bash
{"id":0, "text": "東京 は 今日も 晴れ", "meta": {}, "annotation_approver": null, "comment_count": 0, "labels": [[1,3, "LOCATION"],[6,9,"TIME"]]}
```

## Licence

[MIT](https://en.wikipedia.org/wiki/MIT_License)


