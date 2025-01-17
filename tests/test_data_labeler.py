import unittest
import pandas as pd
from data_labeler import AmharicLabeler

class TestAmharicLabeler(unittest.TestCase):
    def setUp(self):
        self.labeler = AmharicLabeler()
        self.dummy_data = [
            "Under armour Goretex\nSize 40,41,42,43\nPrice 3500 birr\n📌አድራሻ-ሜክሲኮ ኮሜርስ ጀርባ መዚድ ፕላዛ የመጀመሪያ ደረጃ እንደወጡ 101 የቢሮ ቁጥር ያገኙናል or call 0920238243\n                                    [EthioBrand](https://t.me/ethio_brand_collection) ✅",
            "🥳ለጥምቀት እንዲሁም ለተለያዩ በዓላት ወይም ፕሮግራም የሚሆኑ ፥\n\nWhite Sandals\nSize 40,41,42,43,44\nPrice 1900 birr\n📌አድራሻ-ሜክሲኮ ኮሜርስ ጀርባ መዚድ ፕላዛ የመጀመሪያ ደረጃ እንደወጡ 101 የቢሮ ቁጥር ያገኙናል or call 0920238243\n                                    [EthioBrand](https://t.me/ethio_brand_collection) ✅",
            "Nike Air Force Goretex\nSize 40,41,42,43\nPrice 3800 birr\n📌አድራሻ-ሜክሲኮ ኮሜርስ ጀርባ መዚድ ፕላዛ የመጀመሪያ ደረጃ እንደወጡ 101 የቢሮ ቁጥር ያገኙናል or call 0920238243\n                                    [EthioBrand](https://t.me/ethio_brand_collection) ✅",
        ]

    def test_label_tokens(self):
        # Tokenize the dummy data
        tokens = [message.split() for message in self.dummy_data]

        for token_list in tokens:
            labeled_output = self.labeler.label_tokens(token_list)

            # Check if the price has been labeled correctly
            for token, label in labeled_output:
                if "birr" in token:
                    self.assertIn(
                        label,
                        ["I-PRICE", "B-PRICE"],
                        msg=f"Expected a price label for token '{token}' but got '{label}'.",
                    )


if __name__ == "__main__":
    unittest.main()
