CREATE OR REPLACE PROCEDURE sp_retrieving_holders_with_balance_higher_than(searched_balance NUMERIC)
LANGUAGE plpgsql
AS $$
DECLARE
    holder_record RECORD;
BEGIN
    FOR holder_record IN (SELECT CONCAT(first_name, ' ', last_name) AS full_name, SUM(balance) AS total_balance FROM account_holders LEFT JOIN accounts ON account_holders.id = accounts.account_holder_id GROUP BY full_name)
    LOOP
        IF holder_record.total_balance > searched_balance THEN
            RAISE NOTICE '% - %.4f', holder_record.full_name, holder_record.total_balance;
        END IF;
    END LOOP;
END;
$$;
