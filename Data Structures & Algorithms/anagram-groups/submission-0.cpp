class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> hash;

        for (string& str: strs) {
            string key = str;
            sort(key.begin(), key.end());

            if (const auto& iter = hash.find(key); iter != hash.end()) {
                (iter->second).push_back(str);
            } else {
                hash.insert({key, {str}});
            }
        }

        vector<vector<string>> result;        
        for (auto anagram: hash) {
            result.push_back(anagram.second);
        }

        return result;
    }
};
