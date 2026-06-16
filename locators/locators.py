from selenium.webdriver.common.by import By

class Locators:
    # Locators for LogIn
    USERNAME=(By.NAME,"username")
    PASSWORD=(By.NAME,"password")
    LOGIN=(By.XPATH,"//*[@value='Log In']")
    FORGOT_PASSWORD=(By.XPATH,"//*[@href='lookup.htm']")
    REGISTRATION=(By.XPATH,"//*[@href='register.htm']")
    ERROR=(By.XPATH,"//*[text()='Error!']")

    # Locators for Registration
    FNAME=(By.ID,"customer.firstName")
    LNAME=(By.ID,"customer.lastName")
    ADDRESS=(By.ID,"customer.address.street")
    CITY=(By.ID,"customer.address.city")
    STATE=(By.ID,"customer.address.state")
    PIN_CODE=(By.ID,"customer.address.zipCode")
    PHONE=(By.ID,"customer.phoneNumber")
    SSN=(By.ID,"customer.ssn")
    NEW_USERNAME=(By.ID,"customer.username")
    NEW_PASSWORD=(By.ID,"customer.password")
    CONFIRM_PASSWORD=(By.ID,"repeatedPassword")
    REGISTER=(By.XPATH,"//*[@value='Register']")

    # Locators for Account Services
    NEW_ACCOUNT=(By.PARTIAL_LINK_TEXT,"New Account")
    OVERVIEW=(By.PARTIAL_LINK_TEXT,"Overview")
    FUNDS=(By.LINK_TEXT,"Transfer Funds")
    BILL_PAY=(By.PARTIAL_LINK_TEXT,"Bill")
    TRANSACTIONS_INFO=(By.PARTIAL_LINK_TEXT,"Transactions")
    UPDATE_INFO=(By.PARTIAL_LINK_TEXT,"Update Contact")
    Loan=(By.PARTIAL_LINK_TEXT,"Loan")
    LOGOUT=(By.CSS_SELECTOR,"[href='logout.htm']")

    # Locators for Opening New Account
    ACCOUNT_TYPE=(By.ID,"type")
    OLD_ACCOUNT=(By.ID,"fromAccountId")
    OLD_ACCOUNT_WAIT=(By.CSS_SELECTOR,"#fromAccountId option")
    OPEN_ACCOUNT=(By.CSS_SELECTOR,"input.button")
    NEW_ACCOUNT_NUMBER=(By.ID,"newAccountId")

    # Locators for Overview
    ACCOUNT_NUMBER=(By.CSS_SELECTOR,"#accountTable a")

    # Locators for Fund Transfer
    FUND_TRANSFER=(By.CSS_SELECTOR,"[href='transfer.htm']")
    AMOUNT=(By.ID,"amount")
    FROM_ACCOUNT=(By.ID,"fromAccountId")
    TO_ACCOUNT=(By.ID,"toAccountId")
    TRANSFER=(By.XPATH,"//*[@value='Transfer']")
    TRANSFER_COMPLETE=(By.CSS_SELECTOR,"#showResult .title")
    
    
    #Locators for Bill Payment
    BILL_PAY=(By.CSS_SELECTOR,"[href='billpay.htm']")
    PAYEE_NAME=(By.NAME,"payee.name")
    PAYEE_ADDRESS=(By.NAME,"payee.address.street")
    PAYEE_CITY=(By.NAME,"payee.address.city")
    PAYEE_STATE=(By.NAME,"payee.address.state")
    PAYEE_PINCODE=(By.NAME,"payee.address.zipCode")
    PAYEE_PHONE=(By.NAME,"payee.phoneNumber")
    PAYEE_ACCOUNT=(By.NAME,"payee.accountNumber")
    PAYEE_ACCOUNT_VERIFY=(By.NAME,"verifyAccount")
    AMOUNT_PAY=(By.NAME,"amount")
    BILL_ACCOUNT=(By.NAME,"fromAccountId")
    SEND_PAYMENT=(By.XPATH,"//*[@value='Send Payment']")
    
    # Locator to Track Transactions
    TRANSACTIONS=(By.CSS_SELECTOR,"[href='findtrans.htm']")
    ACCOUNT_SELECTION=(By.ID,"accountId")
    TRANSACTION_RESULTS=(By.CSS_SELECTOR,"#resultContainer .title")

    ## Find by Transaction ID
    TRANSACTIONS_ID=(By.ID,"transactionId")
    FIND_BY_ID=(By.ID,"findById")

    ## Find by Date (MM-DD-YYYY)
    TRANSACTIONS_DATE=(By.ID,"transactionDate")
    FIND_BY_DATE=(By.ID,"findByDate")

    ## Find by Date Range (MM-DD-YYYY)
    TRANSACTIONS_FROM_DATE=(By.ID,"fromDate")
    TRANSACTIONS_TO_DATE=(By.ID,"toDate")
    FIND_BY_RANGE=(By.ID,"findByDateRange")

    ## Find by Amount
    TRANSACTIONS_AMOUNT=(By.ID,"amount")
    FIND_BY_AMOUNT=(By.ID,"findByAmount")

    # Locators to Update Info
    UPDATE_CONTACT=(By.CSS_SELECTOR,"[href='updateprofile.htm']")
    UPDATE_FNAME=(By.ID,"customer.firstName")
    UPDATE_LNAME=(By.ID,"customer.lastName")
    UPDATE_ADDRESS=(By.ID,"customer.address.street")
    UPDATE_CITY=(By.ID,"customer.address.city")
    UPDATE_STATE=(By.ID,"customer.address.state")
    UPDATE_PINCODE=(By.ID,"customer.address.zipCode")
    UPDATE_PHONE=(By.ID,"customer.phoneNumber")
    UPDATE_PROFILE=(By.XPATH,"//*[@value='Update Profile']")
    INPUT_BOXES=(By.CSS_SELECTOR,".input")
    VISIBLE=(By.ID,"customer.phoneNumber")

    # Locators to Request Loan
    LOAN_REQUEST=(By.CSS_SELECTOR,"[href='requestloan.htm']")
    LOAN_AMOUNT=(By.ID,"amount")
    DOWN_PAYMENT=(By.ID,"downPayment")
    LOAN_ACCOUNT=(By.ID,"fromAccountId")
    LOAN_APPLY=(By.XPATH,"//*[@value='Apply Now']")
    LOAN_PROCESSED=(By.TAG_NAME,"h1")
    LOAN_STATUS=(By.ID,"loanStatus")