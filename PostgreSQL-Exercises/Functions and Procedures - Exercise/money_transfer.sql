CREATE OR REPLACE PROCEDURE sp_transfer_money(
    sender_id INT,
    receiver_id INT,
    amount NUMERIC(20, 4)
)
LANGUAGE plpgsql
AS $$
DECLARE
    withdraw_successful BOOLEAN := TRUE;
    deposit_successful BOOLEAN := TRUE;
    rows_withdraw INT := 0;
    rows_deposit INT := 0;
BEGIN
    CALL sp_withdraw_money(sender_id, amount);
    GET DIAGNOSTICS rows_withdraw = ROW_COUNT;

    IF rows_withdraw > 0 THEN
        withdraw_successful := FALSE;
    END IF;

    IF withdraw_successful THEN
        CALL sp_deposit_money(receiver_id, amount);
        GET DIAGNOSTICS rows_deposit = ROW_COUNT;

        IF rows_deposit > 0 THEN
            deposit_successful := FALSE;
        END IF;
    END IF;

    IF withdraw_successful AND deposit_successful THEN
        COMMIT;
    ELSE
        ROLLBACK;
    END IF;
END;
$$;
