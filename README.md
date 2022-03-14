# conll-to-jsonl
CoNLL形式からJSONL形式へ変更してくれます。

# Usage

```bash
python CoNLLtoJSONL.py input.conll > output.jsonl
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
{"id":0, "text": "東京は今日も晴れ", "meta": {}, "annotation_approver": null, "comment_count": 0, "labels": [[0,2, "LOCATION"],[3,5,"TIME"]]}
```

## Licence

[MIT](https://en.wikipedia.org/wiki/MIT_License)


