CREATE TABLE notification_emails (
    id SERIAL PRIMARY KEY,
    recipient_id INT NOT NULL,
    subject VARCHAR(50) NOT NULL,
    body VARCHAR(255) NOT NULL
);
CREATE OR REPLACE FUNCTION trigger_fn_send_email_on_balance_change() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO notification_emails (recipient_id, subject, body)
    VALUES (
        NEW.account_id,
        'Balance change for account: ' || NEW.account_id,
        'On ' || TO_CHAR(NOW(), 'YYYY-MM-DD') || ' your balance was changed from ' || ROUND(OLD.new_sum, 2) || ' to ' || ROUND(NEW.new_sum, 2) || '.'
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER tr_send_email_on_balance_change
AFTER UPDATE ON logs
FOR EACH ROW
WHEN (NEW.new_sum != OLD.new_sum)
EXECUTE FUNCTION trigger_fn_send_email_on_balance_change();