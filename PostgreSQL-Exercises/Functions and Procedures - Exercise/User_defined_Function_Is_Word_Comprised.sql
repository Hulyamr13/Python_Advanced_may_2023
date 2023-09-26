CREATE OR REPLACE FUNCTION fn_is_word_comprised(
    set_of_letters VARCHAR(50),
    word VARCHAR(50)
) RETURNS BOOLEAN AS $$
DECLARE
    i INT;
    letter CHAR;
BEGIN
    -- Convert both the set_of_letters and word to lowercase for case-insensitivity
    set_of_letters := LOWER(set_of_letters);
    word := LOWER(word);

    -- Loop through each character in the word
    FOR i IN 1..LENGTH(word) LOOP
        letter := SUBSTRING(word FROM i FOR 1);

        -- Check if the letter exists in the set_of_letters
        IF POSITION(letter IN set_of_letters) = 0 THEN
            RETURN FALSE;
        END IF;
    END LOOP;

    -- If all characters in the word are found in set_of_letters, return TRUE
    RETURN TRUE;
END;
$$ LANGUAGE plpgsql;