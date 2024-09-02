def char_count(text):
    text = text.lower()
    char_freq = {}
    
    for word in text.split(): 
        for char in word.lower():
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1 
    
    return char_freq
            

def main():
    file_path = 'books/frankenstein.txt'
    
    with open(file_path, 'r') as f:
        file_contents = f.read()
        text = file_contents
        char_freq = char_count(text)
    print(f'--- Begin report of {file_path} ---')
    print(f'{len(text.split())} words found in the document')
    
    char_freq_list = list(char_freq.items())
    char_freq_list.sort(key=lambda x: x[1], reverse=True)
    
    for char, freq in char_freq_list: 
        print(f'The {char} character was found {freq} times')
        
    print('--- End report ---')
    
main()
        