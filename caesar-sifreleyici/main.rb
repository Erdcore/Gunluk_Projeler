# Basit Caesar Şifreleyici
# Bu program, kullanıcıdan alınan bir metni verilen kaydırma değeri ile şifreler.

# Alfabenin harfleri (sadece İngilizce küçük harfler kullanılmıştır)
ALPHABET = ('a'..'z').to_a

# Caesar şifreleme fonksiyonu
def caesar_encrypt(text, shift)
  encrypted_text = ""

  text.each_char do |char|
    # Harf olup olmadığını kontrol et
    if ALPHABET.include?(char.downcase)
      is_upper = char == char.upcase  # Harf büyük mü?
      index = ALPHABET.index(char.downcase)
      new_index = (index + shift) % ALPHABET.length
      new_char = ALPHABET[new_index]
      # Eğer orijinal harf büyükse, sonucu büyük yap
      encrypted_text += is_upper ? new_char.upcase : new_char
    else
      # Harf değilse (boşluk, noktalama vs.), olduğu gibi ekle
      encrypted_text += char
    end
  end

  encrypted_text
end

# Kullanıcıdan veri alın
print "Şifrelenecek metni girin: "
input_text = gets.chomp

print "Kaydırma miktarını girin (örneğin 3): "
shift_amount = gets.chomp.to_i

# Şifreleme işlemi
result = caesar_encrypt(input_text, shift_amount)

# Sonucu göster
puts "Şifrelenmiş metin: #{result}"
