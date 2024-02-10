import random
import re
import time
from bs4 import BeautifulSoup
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Clariti.pages.base_page import BasePage, wait_for_file_explorer_open, screenshot_and_attach_report_pyautogui, \
    upload_files, random_string
from Clariti.utilities.locators import Locators


class MailDraftPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # composemail_icon = (By.XPATH, "//im-td-cdrivetabheader//*[contains(text(), 'Compose Mail')]")
    # composemail_icon = (By.XPATH, "//div[@class='iconText' and text()='Compose Mail']")
    # composeMail_icon = (By.CSS_SELECTOR, f"[class*='{'im-tc-startnewcommstrip'}']")
    # subject_field = (By.XPATH, "//input[contains(@class,'im-da-dr-subjectInput')]")
    # to_field_textbox = (By.CSS_SELECTOR, f"[class*='{'im-da-dr-toEmailInput'}']")
    # body_area = (By.CLASS_NAME, "claritioriginalcontent")
    # send_button = (By.XPATH, '//button/span[contains(text(),"Send")]')
    # send_button_class = (By.CSS_SELECTOR, f"[class*='{'im-da-dr-draftcontainerSendBtn'}']")
    # # mat_button_disabled = (By.CSS_SELECTOR, f"[class*='{'mat-button-disabled'}']")
    # mat_button_disabled = (By.CSS_SELECTOR, f"[class*='{'im-da-dr-draftcontainerSendBtn mdc-button'}']")
    # mail_tab = (By.XPATH, "//div[@class='im-ct-menu-title' and text()='Mail ']")
    # detail_view_header_text = (By.CSS_SELECTOR, f"[class*='im-td-cdrivetabheader-drive']")
    # detail_view = (By.CSS_SELECTOR, f"[class*='im-td-cdrivetablayout-root']")
    # clariti_full_view = (By.CSS_SELECTOR, f"[class*='im-app-left-splitter']")
    # close_icon_draft = (By.CSS_SELECTOR, f"[class*='{'im-ct-close'}']")
    # confirmation_button_class = (By.CSS_SELECTOR, f"[class*='im-sc-confirmationdialog-Btn'] span")
    # confirmation_button = (By.CSS_SELECTOR, f"[class*='im-sc-confirmationdialog-Btn mat']")
    # yes_button_to_close_confirmation = (By.XPATH, "//button[contains(., 'Yes')]")
    # draft_area = (By.CSS_SELECTOR, "[class*='im-da-dr-draftcontainer']")
    # draft_layout_contexts_area = (By.CSS_SELECTOR, f"[class*='im-ct-emaildraft-layout']")
    # draft_mail_svg_icon_contexts_area = (By.CSS_SELECTOR, f"[class*='im-ct-ipitem-icon']")
    # draft_text_contexts_area = (By.CSS_SELECTOR, f"[class*='im-ct-activechat-initiator']")
    # draft_subject_contexts_area = (By.CSS_SELECTOR, f"[class*='im-ct-activechat-subject']")
    # # mail_draft_header_text = (By.CSS_SELECTOR, f"[class*='im-td-maildrafttablayout-header']")
    # mail_draft_header_text = (By.CSS_SELECTOR, f"[class*='im-td-maildraft-headingdefault']")

    # draft_to_cc_bcc_field = (By.CSS_SELECTOR, f"[class*='im-da-dr-recipientItem']")
    # draft_to_cc_bcc_label_text = (By.CSS_SELECTOR, f"[class*='im-da-cm-labelPrefix']")
    # draft_to_cc_bcc_add_plus_icon = (By.CSS_SELECTOR, f"[class*='im-da-dr-contactsIconContainer']")
    # draft_cc_bcc_attachment_icon_area = (By.CSS_SELECTOR, f"[class*='im-da-dr-CCRecipientsAttachFiles']")
    # draft_cc_button = (By.CSS_SELECTOR, f"[class*='im-da-dr-showCcMail']")
    # draft_bcc_button = (By.CSS_SELECTOR, f"[class*='im-da-dr-showBccMail']")
    # draft_attachment_icon = (By.CSS_SELECTOR, f"[class*='im-da-dr-AttachFilesIcon']")
    # body_content = (By.CLASS_NAME, "claritioriginalcontent")
    # mail_draft_body = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftcontainerBody']")
    # show_editor_toolbar_icon = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftEditorPullDownArrowContainer']")
    # editor_toolbar = (By.CSS_SELECTOR, f"[class*='im-da-dr-editorToolbar']")
    # editor_toolbar_font_name = (By.CSS_SELECTOR, f"[class*='im-da-dr-fontNameSel']")
    # editor_toolbar_font_size = (By.CSS_SELECTOR, f"[class*='im-da-dr-fontSizeSel']")
    # editor_tool_bold = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarBold']")
    # editor_tool_italic = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarItalic']")
    # editor_tool_strike = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarStrike']")
    # editor_tool_under_line = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarUnderline']")
    # editor_tool_colour = (By.CSS_SELECTOR, f"[class*='im-da-dr-fontColorSel']")
    # editor_tool_colour_icon = (By.CSS_SELECTOR, f"[class*='im-da-dr-fontColorIcon']")
    # editor_tool_colour_list_dialog = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarFontColorList']")
    # editor_tool_colour_list = (By.TAG_NAME, "li")
    # editor_tool_colour_list_item = (By.TAG_NAME, "a")
    # editor_tool_bullet_list = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarBulletList']")
    # editor_tool_number_list = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarNumberList']")
    # editor_tool_reduce_indent = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarReduceIndent']")
    # editor_tool_indent = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarIndent']")
    # editor_tool_left_align = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarJustLeft']")
    # editor_tool_center_align = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarJustCenter']")
    # editor_tool_right_align = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarJustRight']")
    # editor_tool_more_icon = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarInsertTitle']")
    # editor_tool_insert_image_overlay = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarInsertPicture']")
    # editor_tool_insert_hyperlink_overlay = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarInsertLink']")
    # editor_tool_insert_signature_overlay = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarSignature']")
    # editor_tool_reply_to_overlay = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarReplyTo']")
    # bold_tag = (By.TAG_NAME, "b")
    # italic_tag = (By.TAG_NAME, "i")
    # under_line_tag = (By.TAG_NAME, "u")
    # strike_tag = (By.TAG_NAME, "strike")
    # bullet_list_tag = (By.TAG_NAME, "ul")
    # numbered_list_tag = (By.TAG_NAME, "ol")
    # indent_tag = (By.TAG_NAME, "blockquote")
    # image_tag = (By.TAG_NAME, "img")
    # # overlay_action_class = (By.CSS_SELECTOR, f"[class*='mat-menu-content")
    # overlay_action_class = (By.CSS_SELECTOR, f"[class*='mat-mdc-menu-content")
    #
    # button_tag = (By.TAG_NAME, "button")
    # draft_header_area = (By.CSS_SELECTOR, "[class*='im-da-dr-draftcontainerDraftHeader']")
    # to_cc_bcc_label_icon_area = (By.CSS_SELECTOR, f"[class*='im-da-cm-labelPrefix']")
    # to_cc_bcc_label_parent = (By.XPATH, "./ancestor::mat-chip-list")
    # to_cc_bcc_label_icon = (By.CSS_SELECTOR, f"[class*='{'im-da-dr-contactsIconContainer'}']")
    # overlay_container = (By.CSS_SELECTOR, f"[class='cdk-overlay-container']")
    # overlay_pane = (By.CSS_SELECTOR, f"[class='cdk-overlay-pane']")
    # add_participant_dialog = (By.CSS_SELECTOR, f"[class*='im-da-dr-emailtoPos']")
    # add_participant_dialog_header_text = (By.CSS_SELECTOR, f"[class*='im-da-cm-title']")
    # search_contact_text_box = (By.CSS_SELECTOR, f"[class*='im-pa-mc-minicontactlist-searchinput']")
    # add_mail_to_send_mails_text_class = (By.CSS_SELECTOR, f"[class*='im-da-dr-warningText']")
    # draft_footer_send_button_area = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftcontainerSendBtnArea']")
    #
    # add_mail_to_send_mails_text_hyperlink = (By.CSS_SELECTOR, f"[class*='im-da-dr-hyperlink']")
    # send_info_draft_area = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftcontainerSendMsgInfo']")
    # info_message_class = (By.CSS_SELECTOR, f"[class='im-da-dr-draftcontainerSendMsgInfoPopUp']")
    # recipient_error_info = (By.CSS_SELECTOR, f"[class*='im-da-dr-messagelistErrorMessages']")
    # subject_error_info = (By.CSS_SELECTOR, f"[class*='im-da-dr-messagelistWarningMessages']")
    #
    # add_mail_to_send_mails_text = "Add mail account to send mails"
    # integration_breadcrumb_header = (By.CSS_SELECTOR, f"[class*='im-np-up-profiledetail-breadcrumb-container']")
    # send_mail_enabled_premium_subscription_text = "Send mail is enabled with Premium subscription"
    # remove_contact_icon = (By.CSS_SELECTOR, f"[class*='im-da-cm-remove']")
    # upgrade_alert_dialog = (By.CSS_SELECTOR, f"[class*='im-sh-paymentupgrade-text']")
    # upgrade_dialog_close_icon = (By.CSS_SELECTOR, f"[class*='im-da-cm-mccloseicon']")
    # overlay_close_click_anywhere = (By.CSS_SELECTOR, f"[class*='cdk-overlay-container']")
    # overlay_mail_draft = (By.CSS_SELECTOR, f"[class*='im-td-cdrive-detailsOverlay']")
    # add_contact_overlay = (By.CSS_SELECTOR, f"[class*='im-td-shareemailitem']")
    # maximum_10_files_alert = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftcontainerInvalidAttachMessageContainer']")
    # maximum_10_files_alert_info_icon = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftcontainerAttachInfoIcon']")
    # file_attachment_area = (By.CSS_SELECTOR, f"[class*='im-da-dr-draftcontainerAttachmentList']")
    # file_attachments = (By.CSS_SELECTOR, f"[class*='im-da-cm-fileContainer']")
    # file_attachment_name = (By.CSS_SELECTOR, f"[class*='attachImgIcon-fileName']")
    # file_attachment_delete_icon = (By.CSS_SELECTOR, f"[class*='im-da-cm-deleteIconClass']")
    # file_attachment_svg_icon = (By.CSS_SELECTOR, f"[class*='im-da-cm-imageContainer']")
    # file_attachment_cancel_upload = (By.CSS_SELECTOR, f"[class*='im-da-cm-cancelUploadIcon']")
    # overlay_tooltip = (By.CSS_SELECTOR, f"[class*='mdc-tooltip__surface-animation']")
    # overlay_dialog = (By.CSS_SELECTOR, "[class*='im-td-detailsoverlay-container']")
    # overlay_dialog_title = (By.CSS_SELECTOR, f"[class*='im-shareitems-title']")
    # close_icon_overlay = (By.CSS_SELECTOR, "[class*='im-td-overlayClose-icon']")
    # overlay_search_textbox = (By.CSS_SELECTOR, f"[class*='{'im-cm-share-searchTextBox'}']")
    # mail_draft_layout = (By.CSS_SELECTOR, "[class*='im-td-maildrafttablayout-root']")
    # table_body = (By.XPATH, '//*[contains(@class, "im-pa-mc-contact-tablebody")]')
    # rows = (By.CSS_SELECTOR, f"[class*='{'im-table-row ng-star-inserted'}']")
    # subject_class = (By.CSS_SELECTOR, f"[class*='{'im-pa-mc-contact-textname'}']")
    # no_contacts_found_alert = (By.XPATH, '//*[contains(@class, "im-pa-mc-no-contacts")]')
    # contact_table = (By.CSS_SELECTOR, f"[class*='{'im-shareitems-contacttable'}']")
    # # focused_textbox_hyperlink = (By.CSS_SELECTOR, f"[class*='mat-focused']")
    # focused_textbox_hyperlink = (By.CSS_SELECTOR, f"[class*='mdc-floating-label--float-above']")
    # hyperlink_url_text_textbox = (By.CSS_SELECTOR, f"[class*='im-da-dr-urltext'] input")
    # hyperlink_url_textbox = (By.CSS_SELECTOR, f"[class*='im-da-dr-url n'] input")
    # hyperlink_insert_button = (By.CSS_SELECTOR, f"[class*='im-da-dr-okBtn']")
    # hyperlink_preview_link = (By.CSS_SELECTOR, f"[class*='im-da-dr-hyperLink']")
    # # hyperlink_error_not_a_valid_url = (By.CSS_SELECTOR, f"[class*='mat-error']")
    # hyperlink_error_not_a_valid_url = (By.CSS_SELECTOR, f"[class*='mat-mdc-form-field-error']")
    #
    # hyperlink_dialog_close = (By.CSS_SELECTOR, f"[class*='im-da-cm-mcclose']")
    # mini_contact_list_overlay = (
    #     By.CSS_SELECTOR, f"[class*='{'im-cm-sh-sharelist-list'}']")  # Updated from im-pa-mc-minicontactlist-itemlist
    # contact_list_overlay = (By.CSS_SELECTOR, "[class*='im-sc-participant-myChatContact']")
    # mini_contact_container_overlay = (
    #     By.CSS_SELECTOR,
    #     f"[class*='{'im-cm-sh-sharelist-container'}']")  # Updated from im-pa-mc-minicontactlist-container
    # mini_contact_container_main_overlay = (By.CSS_SELECTOR, f"[class*='{'im-pa-sh-mpw-body'}']")
    # scroll_area_overlay = (By.CSS_SELECTOR, f"[class*='{'ps__rail-y'}']")  # Updated from ps--active-y
    # scroll_bar_overlay = (By.CSS_SELECTOR, f"[class*='{'ps__thumb-y'}']")
    # contact_click_overlay = (By.CSS_SELECTOR, 'button[type="button"]')
    # hyperlink_dialog = (By.CSS_SELECTOR, f"[class*='im-da-dr-parentContainer']")
    # signature_dialog = (By.CSS_SELECTOR, f"[class*='im-da-dr-signatureDraftEditor']")
    # checkbox_area = (By.CSS_SELECTOR, f"[class*='im-da-dr-signatureCheckBox']")
    # #checkbox_input = (By.CSS_SELECTOR, f"[class*='mat-checkbox-input']")
    # checkbox_input = (By.CSS_SELECTOR, f"[class*='mdc-checkbox__native-control']")
    # reply_to_textbox = (By.CSS_SELECTOR, f"[class*='im-da-dr-replyto'] input")
    # reply_to_msg_draft = (By.CSS_SELECTOR, f"[class*='im-da-dr-replyToMsg']")
    # reply_to_msg_draft_label_text = "Reply for this email will be sent to"
    # mail_will_be_sent_using = (By.CSS_SELECTOR, f"[class*='{'im-da-dr-fromidComp'}']")
    # mail_will_be_sent_using_email_id = (By.CSS_SELECTOR, f"[class*='im-da-dr-selectedMailId']")
    # mail_will_be_sent_using_email_id_drop_down = (By.CSS_SELECTOR, f"[class*='im-da-dr-selectFromEmailIDs']")
    #
    # # Enter Body content in 1st Line.
    # draft_body_text = (By.CSS_SELECTOR, f"[class*='claritioriginalcontent'] div")
    # draft_body_text_tab = (By.CSS_SELECTOR, f"[class*='claritioriginalcontent'] br")
    # draft_body = (By.CSS_SELECTOR, f"[class*='claritioriginalcontent']")

    def click_to_close_dialog_overlay(self):
        self.click(Locators.MailDraftPage.OVERLAY_CLOSE_CLICK_ANYWHERE)

    def body_content_message(self, tab_or_overlay, message):
        # self.click(Locators.MailDraftPage.BODY_AREA)
        # for _ in range(4):
        #     self.send_keys(Locators.MailDraftPage.BODY_AREA, Keys.UP)
        # # self.keyboard_usage(Locators.MailDraftPage.BODY_AREA, Keys.UP, 4)
        if tab_or_overlay == "tab":
            # self.send_keys(Locators.MailDraftPage.DRAFT_BODY_TEXT_TAB, message)
            self.click(Locators.MailDraftPage.BODY_AREA)
            for _ in range(4):
                self.send_keys(Locators.MailDraftPage.BODY_AREA, Keys.UP)
            self.send_keys(Locators.MailDraftPage.BODY_AREA, message)
        elif tab_or_overlay == "overlay":
            OverlayDraft = self.get_element(Locators.MailDraftPage.OVERLAY_MAIL_DRAFT)
            OverlayDraftBody = OverlayDraft.find_element(*Locators.MailDraftPage.DRAFT_BODY_TEXT)
            self.send_keys(OverlayDraftBody, message)

    def enter_body_content(self, draft_message):
        self.send_keys(Locators.MailDraftPage.DRAFT_BODY_TEXT, draft_message)

    def click_compose_mail_button(self):
        self.close_mail_overlay()
        self.click(Locators.MailDraftPage.COMPOSE_MAIL_ICON)

    def close_mail_overlay(self):
        try:
            CloseIcon = self.get_element(Locators.MailDraftPage.CLOSE_ICON_OVERLAY)
            if CloseIcon.is_displayed():
                CloseIcon.click()
        except NoSuchElementException:
            pass

    def click_send_button(self):
        self.click(Locators.MailDraftPage.SEND_BUTTON)

    def enter_to_address(self, email):
        self.send_keys(Locators.MailDraftPage.TO_FIELD_TEXTBOX, email)

    def click_mail_tab(self):
        self.click(Locators.MailDraftPage.MAIL_TAB)

    def click_to_close_add_participant_dialog(self):
        self.click(Locators.MailDraftPage.OVERLAY_CONTAINER)

    def enter_subject(self, subject):
        self.send_keys(Locators.MailDraftPage.SUBJECT_FIELD, subject)

    def mail_send(self, subject, sent_to, email, tab_or_overlay, message):
        self.click(Locators.MailDraftPage.MAIL_TAB)
        time.sleep(1)
        self.click(Locators.MailDraftPage.COMPOSE_MAIL_ICON)
        self.send_keys(Locators.MailDraftPage.SUBJECT_FIELD, subject)
        time.sleep(0.5)
        if sent_to == "TO":
            self.send_keys(Locators.MailDraftPage.TO_FIELD_TEXTBOX, email)
        time.sleep(0.5)
        self.click(Locators.MailDraftPage.BODY_AREA)
        self.body_content_message(tab_or_overlay, message)
        time.sleep(2)
        # self.send_keys(Locators.MailDraftPage.BODY_AREA, message)
        self.click(Locators.MailDraftPage.SEND_BUTTON)

    def sending_mail_after_draft_opened(self, subject, sent_to, email, tab_or_overlay, message):
        self.send_keys(Locators.MailDraftPage.SUBJECT_FIELD, subject)
        time.sleep(0.5)
        if sent_to == "TO":
            self.send_keys(Locators.MailDraftPage.TO_FIELD_TEXTBOX, email)
        time.sleep(0.5)
        self.click(Locators.MailDraftPage.BODY_AREA)
        self.body_content_message(tab_or_overlay, message)
        time.sleep(2)
        self.click(Locators.MailDraftPage.SEND_BUTTON)

    def mail_send_dummy(self, subject, sent_to, email, tab_or_overlay, message):
        self.click(Locators.MailDraftPage.MAIL_TAB)
        time.sleep(1)
        self.click(Locators.MailDraftPage.COMPOSE_MAIL_ICON)
        self.send_keys(Locators.MailDraftPage.SUBJECT_FIELD, subject)
        if sent_to == "TO":
            self.send_keys(Locators.MailDraftPage.TO_FIELD_TEXTBOX, email)
        self.click(Locators.MailDraftPage.BODY_AREA)
        self.body_content_message(tab_or_overlay, message)
        time.sleep(0.2)
        # self.send_keys(Locators.MailDraftPage.BODY_AREA, message)
        self.click(Locators.MailDraftPage.SEND_BUTTON)

    def mail_send_2_users(self, subject, sent_to, email1, email2, tab_or_overlay, message):
        self.click(Locators.MailDraftPage.MAIL_TAB)
        time.sleep(1)
        self.click(Locators.MailDraftPage.COMPOSE_MAIL_ICON)
        self.send_keys(Locators.MailDraftPage.SUBJECT_FIELD, subject)
        if sent_to == "TO":
            self.send_keys(Locators.MailDraftPage.TO_FIELD_TEXTBOX, email1 + Keys.ENTER)
            time.sleep(0.5)
            self.send_keys(Locators.MailDraftPage.TO_FIELD_TEXTBOX, email2 + Keys.ENTER)
        else:
            print("Enter proper sent to like 'TO/CC/BCC'")

        self.click(Locators.MailDraftPage.BODY_AREA)
        self.body_content_message(tab_or_overlay, message)
        # self.send_keys(Locators.MailDraftPage.BODY_AREA, message)
        self.click(Locators.MailDraftPage.SEND_BUTTON)

    def click_add_from_your_contacts_icon(self, prefix):  # Prefix Means To / CC / BCC
        DraftHeader = self.get_element(Locators.MailDraftPage.DRAFT_HEADER_AREA)
        label_prefix = DraftHeader.find_elements(*Locators.MailDraftPage.TO_CC_BCC_LABEL_ICON_AREA)
        # print(len(label_prefix))
        for prefixes in label_prefix:
            # print(prefixes.text)
            if prefixes.text == prefix:
                ParentElement = prefixes.find_element(*Locators.MailDraftPage.TO_CC_BCC_LABEL_PARENT)
                ParentElement.find_element(*Locators.MailDraftPage.TO_CC_BCC_LABEL_ICON).click()

    def click_search_text_box_add_participant_dialog(self, contact_name):
        AddParticipantDialogOverlay = self.get_element(Locators.MailDraftPage.ADD_PARTICIPANT_DIALOG)
        AddParticipantDialogOverlay.find_element(*Locators.MailDraftPage.SEARCH_CONTACT_TEXT_BOX).send_keys(contact_name)

    def click_show_editor_toolbar_icon(self):
        MailDraftBodyArea = self.get_element(Locators.MailDraftPage.MAIL_DRAFT_BODY)
        action = ActionChains(self.driver)
        action.move_to_element(MailDraftBodyArea).perform()
        self.click(Locators.MailDraftPage.SHOW_EDITOR_TOOLBAR_ICON)

    def click_editor_font_name(self):
        self.click(Locators.MailDraftPage.EDITOR_TOOLBAR_FONT_NAME)
        # FontName = self.get_element(Locators.MailDraftPage.EDITOR_TOOLBAR_font_name)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(FontName).perform()
        # time.sleep(0.5)
        # FontName.click()

    def click_editor_font_size(self):
        self.click(Locators.MailDraftPage.EDITOR_TOOLBAR_FONT_SIZE)
        # FontSize = self.get_element(Locators.MailDraftPage.EDITOR_TOOLBAR_font_size)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(FontSize).perform()
        # time.sleep(0.5)
        # FontSize.click()

    def click_editor_bold(self):
        self.click(Locators.MailDraftPage.EDITOR_TOOL_BOLD)

    def click_editor_italic(self):
        self.click(Locators.MailDraftPage.EDITOR_TOOL_ITALIC)

    def click_editor_strike_through(self):
        self.click(Locators.MailDraftPage.EDITOR_TOOL_STRIKE)

    def click_editor_underline(self):
        self.click(Locators.MailDraftPage.EDITOR_TOOL_UNDER_LINE)

    def click_editor_colour(self):
        self.click(Locators.MailDraftPage.EDITOR_TOOL_COLOUR)

    def click_editor_bullet_list(self):
        self.click(Locators.MailDraftPage.EDITOR_TOOL_BULLET_LIST)

    def click_editor_numbered_list(self):
        self.click(Locators.MailDraftPage.EDITOR_TOOL_NUMBER_LIST)

    def click_editor_indent(self):
        self.click(Locators.MailDraftPage.EDITOR_TOOL_INDENT)

    def click_editor_reduce_indent(self):
        self.click(Locators.MailDraftPage.EDITOR_TOOL_REDUCE_INDENT)

    def click_editor_left_align(self):
        self.click(Locators.MailDraftPage.EDITOR_TOOL_LEFT_ALIGN)

    def click_editor_center_align(self):
        self.click(Locators.MailDraftPage.EDITOR_TOOL_CENTER_ALIGN)

    def click_editor_right_align(self):
        self.click(Locators.MailDraftPage.EDITOR_TOOL_RIGHT_ALIGN)

    def click_editor_more_icon(self):
        self.click(Locators.MailDraftPage.EDITOR_TOOL_MORE_ICON)

    def click_editor_insert_image(self):
        self.click_editor_more_icon()
        time.sleep(0.5)
        overlay = self.get_element(Locators.MailDraftPage.OVERLAY_CONTAINER)
        overlay.find_element(*Locators.MailDraftPage.EDITOR_TOOL_INSERT_IMAGE_OVERLAY).click()

    def click_editor_insert_hyperlink(self):
        self.click_editor_more_icon()
        time.sleep(0.5)
        overlay = self.get_element(Locators.MailDraftPage.OVERLAY_CONTAINER)
        overlay.find_element(*Locators.MailDraftPage.EDITOR_TOOL_INSERT_HYPERLINK_OVERLAY).click()

    def click_editor_signature(self):
        self.click_editor_more_icon()
        time.sleep(0.5)
        overlay = self.get_element(Locators.MailDraftPage.OVERLAY_CONTAINER)
        overlay.find_element(*Locators.MailDraftPage.EDITOR_TOOL_INSERT_SIGNATURE_OVERLAY).click()
        self.wait_for_element(Locators.MailDraftPage.SIGNATURE_DIALOG)

    def verify_tool_editor_content(self):
        Parent = self.get_element(Locators.MailDraftPage.BODY_CONTENT)
        try:
            if Parent.find_element(*Locators.MailDraftPage.BOLD_TAG):
                child_b_element = Parent.find_element(*Locators.MailDraftPage.BOLD_TAG).text
                print(child_b_element)
        except:
            print("Bold Content Not Found")

    def wait_for_draft_opened(self):
        self.wait_for_element(Locators.MailDraftPage.ADD_MAIL_TO_SEND_MAILS_TEXT_CLASS)

    def wait_for_draft_opened_mail_configured(self):
        self.wait_for_element(Locators.MailDraftPage.SEND_INFO_DRAFT_AREA)

    def verify_draft_opened(self):
        self.wait_for_element(Locators.MailDraftPage.ADD_MAIL_TO_SEND_MAILS_TEXT_CLASS)
        if Locators.MailDraftPage.ADD_MAIL_TO_SEND_MAILS_TEXT_CLASS:
            print("mail Draft Opened")
            self.screenshot_and_attach_report(Locators.MailDraftPage.CLARITI_FULL_VIEW, "MailDraftOpened",
                                              "Verify Mail Draft Opened or Not")
            return True
        else:
            print("mail Draft not Opened")
            self.screenshot_and_attach_report(Locators.MailDraftPage.CLARITI_FULL_VIEW, "MailDraftOpened",
                                              "Verify Mail Draft Opened or Not")
            return False

    def verify_draft_opened_mail_configured(self):
        self.wait_for_element(Locators.MailDraftPage.DRAFT_FOOTER_SEND_BUTTON_AREA)
        if Locators.MailDraftPage.DRAFT_FOOTER_SEND_BUTTON_AREA:
            print("mail Draft Opened")
            self.screenshot_and_attach_report(Locators.MailDraftPage.CLARITI_FULL_VIEW, "MailDraftOpened",
                                              "Verify Mail Draft Opened or Not")
            return True
        else:
            print("mail Draft not Opened")
            self.screenshot_and_attach_report(Locators.MailDraftPage.CLARITI_FULL_VIEW, "MailDraftOpened",
                                              "Verify Mail Draft Opened or Not")
            return False

    def close_mail_draft(self):
        self.click(Locators.MailDraftPage.CLOSE_ICON_DRAFT)
        time.sleep(2)
        self.click(Locators.MailDraftPage.YES_BUTTON_TO_CLOSE_CONFIRMATION)
        time.sleep(1)
        # ConfirmationDialog = self.get_text(Locators.MailDraftPage.CONFIRMATION_BUTTON_CLASS)
        # if " Yes " == ConfirmationDialog:
        #     self.click(self.confirmation_button)

    # Verify Add Mail account to send Mails.
    # Dated on 23.10.2023
    def verify_add_mail_to_send_mails(self):
        AddText = self.get_element(Locators.MailDraftPage.ADD_MAIL_TO_SEND_MAILS_TEXT_CLASS)
        inner_html = AddText.get_attribute("innerHTML")
        # Parse the inner HTML with BeautifulSoup
        soup = BeautifulSoup(inner_html, "html.parser")
        # Extract and merge the text from the <a> and <span> elements
        JoinMultiLineText = ' '.join(soup.stripped_strings)
        print(JoinMultiLineText)

        if Locators.MailDraftPage.ADD_MAIL_TO_SEND_MAILS_TEXT in JoinMultiLineText:
            print("Alert info appears")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "AddMailsAlert",
                                              "Verify Add Mail account to send mail alert appears")
            return True
        else:
            print("Alert not appears")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "AddMailsAlert",
                                              "Verify Add Mail account to send mail alert Not Appears")
            return False

    def click_add_button_in_add_mail_to_send_mails_text(self):
        AddText = self.get_element(Locators.MailDraftPage.ADD_MAIL_TO_SEND_MAILS_TEXT_CLASS)
        AddHyperlinkText = AddText.find_element(*Locators.MailDraftPage.ADD_MAIL_TO_SEND_MAILS_TEXT_HYPERLINK)
        AddHyperlinkText.click()

    def verify_add_mail_ui_clicking_add_mails(self):
        self.click_add_button_in_add_mail_to_send_mails_text()
        time.sleep(1)
        Header = self.get_text(Locators.MailDraftPage.INTEGRATION_BREADCRUMB_HEADER)
        if "Add Mail" in Header:
            print("Add mail Ui Navigated")
            screenshot_and_attach_report_pyautogui("AddMailUINavigated", "Verify Add Mail UI navigated clicking Add button.")
            return True
        else:
            print("Add mail Ui not Navigated")
            screenshot_and_attach_report_pyautogui("AddMailUINotNavigated", "Verify Add Mail UI navigated clicking Add button.")
            return False

    def verify_send_mail_enabled_with_premium(self):
        sendMailText = self.get_element(Locators.MailDraftPage.ADD_MAIL_TO_SEND_MAILS_TEXT_CLASS)
        inner_html = sendMailText.get_attribute("innerHTML")
        # Parse the inner HTML with BeautifulSoup
        soup = BeautifulSoup(inner_html, "html.parser")
        # Extract and merge the text from the <a> and <span> elements
        JoinMultiLineText = ' '.join(soup.stripped_strings)
        print(JoinMultiLineText)

        if Locators.MailDraftPage.SEND_MAIL_ENABLED_PREMIUM_SUBSCRIPTION_TEXT in JoinMultiLineText:
            print("Alert info appears")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "PremiumSubscriptionAlert",
                                              "Send mail is enabled with premium subscription alert")
            return True
        else:
            print("Alert not appears")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "PremiumSubscriptionAlert",
                                              "Send mail is enabled with premium subscription alert Not Appears")
            return False

    # Verify Bold text available in Draft Body,.
    # Dated on 23.10.2023
    def verify_bold_content(self):
        BodyContent = self.get_element(Locators.MailDraftPage.DRAFT_BODY)
        if BodyContent:
            try:
                bold_tag = BodyContent.find_element(Locators.MailDraftPage.BOLD_TAG)
                if bold_tag:
                    print("Bold Exists")
            except:
                print("Bold Not Exists")

    def verify_cursor_active_subject(self):
        text_box = self.get_element(Locators.MailDraftPage.SUBJECT_FIELD)
        is_active_element = text_box == self.driver.switch_to.active_element
        if is_active_element:
            print("The text box is the currently active element")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "SubjectCursorTextBox",
                                              "Cursor is focused in subject Field")
            return True
        else:
            print("The text box is not the currently active element")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "SubjectCursorTextBox",
                                              "Cursor is not focused in subject Field")
            return False

    def verify_draft_subject_text_context_area(self):
        Draft = self.get_elements(Locators.MailDraftPage.DRAFT_LAYOUT_CONTEXTS_AREA)
        for eachDraft in Draft:
            GetMailIcon = eachDraft.find_element(*Locators.MailDraftPage.DRAFT_MAIL_SVG_ICON_CONTEXTS_AREA)
            GetDraftText = eachDraft.find_element(*Locators.MailDraftPage.DRAFT_TEXT_CONTEXTS_AREA).text
            GetSubjectText = eachDraft.find_element(*Locators.MailDraftPage.DRAFT_SUBJECT_CONTEXTS_AREA).text
            if GetDraftText == "Draft" and GetSubjectText == "no subject" and GetMailIcon:
                print("New Draft Opened with Draft text and No subject text")
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_LAYOUT_CONTEXTS_AREA, "NewDraftOpened",
                                                  "Verify Draft text and no subject text and Mail icon in Mail Draft")
                return True
            else:
                print("New Draft not opened with Draft text or No subject text")
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_LAYOUT_CONTEXTS_AREA, "NewDraftOpened",
                                                  "Verify Draft text and no subject text and Mail icon in Mail Draft")
                return False

    def verify_draft_header_text(self):
        GetDraftHeaderText = self.get_text(Locators.MailDraftPage.MAIL_DRAFT_HEADER_TEXT)
        if GetDraftHeaderText == "New mail":
            print("New mail text appears in Draft")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_HEADER_TEXT, "NewDraftHeaderText",
                                              "Verify Draft Header text")
            return True

        else:
            print("New Mail text not appears")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_HEADER_TEXT, "NewDraftHeaderText",
                                              "Verify Draft Header text")
            return False

    def verify_subject_placeholder_text(self):
        SubjectFieldArea = self.get_element(Locators.MailDraftPage.SUBJECT_FIELD)
        placeholder_text = SubjectFieldArea.get_attribute("placeholder")
        if placeholder_text == "Subject":
            print("PlaceHolder text -" + placeholder_text + " appears in Draft")
            self.screenshot_and_attach_report(Locators.MailDraftPage.SUBJECT_FIELD, "SubjectPlaceholderText",
                                              "Verify subject Field placeHolder text in Draft")
            return True

        else:
            print("PlaceHolder text -" + placeholder_text + " not appears in Draft")
            self.screenshot_and_attach_report(Locators.MailDraftPage.SUBJECT_FIELD, "SubjectPlaceholderText",
                                              "Verify subject Field placeHolder text in Draft")
            return False

    def enter_subject_and_verify_contexts_area(self, subject):
        self.send_keys(Locators.MailDraftPage.SUBJECT_FIELD, subject)
        time.sleep(2)
        GetSubjectText = self.get_text(Locators.MailDraftPage.DRAFT_SUBJECT_CONTEXTS_AREA)
        if GetSubjectText == subject:
            print("New Draft subject Updated to Entered subject - " + subject)
            self.screenshot_and_attach_report(Locators.MailDraftPage.SUBJECT_FIELD, "DraftSubjectEntered",
                                              "Verify Draft subject Entered in mail Draft ")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_LAYOUT_CONTEXTS_AREA,
                                              "DraftSubjectEnteredUpdatedInContextsArea",
                                              "Verify Draft subject Entered and entered subject updated in Draft "
                                              "Contexts Area")
            return True

        else:
            print("New Draft subject not Updated to Entered subject - " + subject)
            self.screenshot_and_attach_report(Locators.MailDraftPage.SUBJECT_FIELD, "DraftSubjectEntered",
                                              "Verify Draft subject Entered in mail Draft ")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_LAYOUT_CONTEXTS_AREA,
                                              "DraftSubjectEnteredUpdatedInContextsArea",
                                              "Verify Draft subject Entered and entered subject updated in Draft "
                                              "Contexts Area")
            return False

    def click_add_participant_dialog(self, field):
        if field == "Cc":
            CcButtonArea = self.get_element(Locators.MailDraftPage.DRAFT_CC_BCC_ATTACHMENT_ICON_AREA)
            CcButtonArea.find_element(*Locators.MailDraftPage.DRAFT_CC_BUTTON).click()
            time.sleep(1)
        elif field == "Bcc":
            BccButtonArea = self.get_element(Locators.MailDraftPage.DRAFT_CC_BCC_ATTACHMENT_ICON_AREA)
            BccButtonArea.find_element(*Locators.MailDraftPage.DRAFT_BCC_BUTTON).click()
            time.sleep(1)
        ToCcBccField = self.get_elements(Locators.MailDraftPage.DRAFT_TO_CC_BCC_FIELD)
        for eachDraft in ToCcBccField:
            GetField = eachDraft.find_element(*Locators.MailDraftPage.TO_CC_BCC_LABEL_ICON_AREA)
            if GetField.text == field:
                eachDraft.find_element(*Locators.MailDraftPage.DRAFT_TO_CC_BCC_ADD_PLUS_ICON).click()
                time.sleep(0.5)
                return True

    def verify_add_participant_dialog(self, field):
        ToCcBccField = self.get_elements(Locators.MailDraftPage.DRAFT_TO_CC_BCC_FIELD)
        for eachDraft in ToCcBccField:
            GetField = eachDraft.find_element(*Locators.MailDraftPage.TO_CC_BCC_LABEL_ICON_AREA)
            if GetField.text == field:
                eachDraft.find_element(*Locators.MailDraftPage.DRAFT_TO_CC_BCC_ADD_PLUS_ICON).click()
                time.sleep(0.5)
                # AddDialog = self.get_element(Locators.MailDraftPage.ADD_PARTICIPANT_DIALOG)
                # TitleText = AddDialog.find_element(*Locators.MailDraftPage.ADD_PARTICIPANT_DIALOG_HEADER_TEXT).text
                # Overlay Type
                AddDialog = self.get_element(Locators.MailDraftPage.OVERLAY_DIALOG)
                TitleText = AddDialog.find_element(*Locators.MailDraftPage.OVERLAY_DIALOG_TITLE).text
                recipient_type = TitleText[16:-1]  # Extract "To", "Cc", or "Bcc"
                if recipient_type == field:
                    print("Add contact to '" + field + "' - Dialog Opened")
                    self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "AddContactDialog",
                                                      "Verify Respective Add contact Dialog Opened ")
                    return True
                else:
                    print(f"Invalid recipient type: {recipient_type}")
                    print(field + "- Dialog not Opened")
                    self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "AddContactDialog",
                                                      "Verify Respective Add contact Dialog Opened ")
                    return False

            else:
                print("Given Field Not Available")
                self.screenshot_and_attach_report(Locators.MailDraftPage.DETAIL_VIEW, "AddContactDialog",
                                                  "Verify Respective Add contact Dialog Opened ")
                return False

    def verify_upgrade_alert_adding_support(self):
        UpgradeAlert = self.get_text(Locators.MailDraftPage.UPGRADE_ALERT_DIALOG)
        if "You can communicate with Clariti Support only in paid subscription plans" in UpgradeAlert:
            print("Upgrade Dialog Appears")
            self.screenshot_and_attach_report(Locators.MailDraftPage.CLARITI_FULL_VIEW, "UpgradeAlert",
                                              "Verify Upgrade Alert Appears while Adding Clariti Support ")
            return True
        else:
            print("Upgrade Dialog not Appears")
            self.screenshot_and_attach_report(Locators.MailDraftPage.CLARITI_FULL_VIEW, "UpgradeAlert",
                                              "Verify Upgrade Alert Appears while Adding Clariti Support ")
            return False

    def close_upgrade_dialog(self):
        self.click(Locators.MailDraftPage.UPGRADE_DIALOG_CLOSE_ICON)

    def is_contact_visible(self, contact_name):
        # contact_list = self.get_element(Locators.MailDraftPage.MINI_CONTACT_LIST_OVERLAY)
        # contact_elements = contact_list.find_elements(*Locators.MailDraftPage.CONTACT_LIST_OVERLAY)
        # for element in contact_elements:
        #     # co=element.text
        #     # print(co)
        #     # if contact_name.lower() in co.lower():
        #     if element.text.lower() == contact_name.lower():
        #         # print(element)
        #         # element.click()
        #         return True
        # return False
        try:
            table = self.get_element(Locators.MailDraftPage.TABLE_BODY)
            if table.is_displayed():

                # Initialize a variable to store the found row
                found_row = None
                while found_row is None:
                    rows = table.find_elements(*Locators.MailDraftPage.ROWS)

                    # Iterate over the rows and check the conditions
                    for row in rows:
                        # Get the subject cell
                        subject_cell = row.find_elements(*Locators.MailDraftPage.SUBJECT_CLASS)
                        for cell in subject_cell:
                            if cell.text.lower() == contact_name.lower():
                                found_row = row
                                break
                        if found_row is not None:
                            return found_row

                if found_row is None:
                    print("contact not found")
                    return None
        except:
            NoContacts = self.get_element(Locators.MailDraftPage.NO_CONTACTS_FOUND_ALERT)
            if NoContacts.is_displayed():
                print("No Contacts found Alert appears")
                return None

    # This function used in contact_selection_ip_chat
    def hover_and_scroll(self, contact_list):
        # Find the scrollbar element
        ContactMiniContainer = self.get_element(Locators.MailDraftPage.CONTACT_TABLE)
        ScrollClass = ContactMiniContainer.find_element(*Locators.MailDraftPage.SCROLL_AREA_OVERLAY)
        scrollbar = ScrollClass.find_element(*Locators.MailDraftPage.SCROLL_BAR_OVERLAY)

        # Create an ActionChains instance
        actions = ActionChains(self.driver)

        # Hover over the scrollbar element and perform the scroll action
        actions.move_to_element(scrollbar).click_and_hold().move_by_offset(0, 30).release().perform()
        # time.sleep(3)

        # Wait for a new element to be present
        WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located(Locators.MailDraftPage.TABLE_BODY))

        actions.move_to_element(scrollbar).click_and_hold().move_by_offset(0, 3).release().perform()

        # Find the updated contact list element
        contact_list = self.get_element(Locators.MailDraftPage.TABLE_BODY)
        print("contact list updated")
        con = contact_list.text
        # print(con)
        # Return the updated contact list element
        return contact_list

    # This function used in contact_selection_ip_chat
    def check_contact_visibility(self, contact_name):
        visible = self.is_contact_visible(contact_name)
        contact_list = self.get_element(Locators.MailDraftPage.TABLE_BODY)
        previous_contact_list_text = contact_list.text
        # Find the parent element containing the contacts
        contact_list = self.get_element(Locators.MailDraftPage.TABLE_BODY)

        while not visible:
            self.hover_and_scroll(contact_list)
            contact_list1 = self.get_element(Locators.MailDraftPage.TABLE_BODY)
            current_contact_list_text = contact_list1.text

            if current_contact_list_text == previous_contact_list_text:
                print("No contact exists")
                break

            c = contact_list1.text
            # print(c)
            visible = self.is_contact_visible(contact_name)
            previous_contact_list_text = current_contact_list_text

    def verify_contact_selection_dialog(self, contact_name):
        visible = self.is_contact_visible(contact_name)
        if visible:
            self.screenshot_and_attach_report(Locators.MailDraftPage.OVERLAY_DIALOG, "AddParticipantDialogContactSearch",
                                              "Verify searched contact appearing in Add contact search results")
            return True
        # If not visible, scroll down and check again
        if not visible:
            self.check_contact_visibility(contact_name)
            self.screenshot_and_attach_report(Locators.MailDraftPage.OVERLAY_DIALOG, "AddParticipantDialogContactSearch",
                                              "Verify searched contact appearing in Add contact search results")

        time.sleep(1)

    def enter_search_contact_results_add_participant(self, contact_name):
        # AddParticipantDialog = self.get_element(Locators.MailDraftPage.ADD_PARTICIPANT_DIALOG)
        # SearchTextBox = AddParticipantDialog.find_element(*Locators.MailDraftPage.SEARCH_CONTACT_TEXT_BOX)
        # self.send_keys(SearchTextBox, contact_name)
        # Overlay Code Updated 6.11.2023
        AddParticipantDialog = self.get_element(Locators.MailDraftPage.OVERLAY_DIALOG)
        SearchTextBox = AddParticipantDialog.find_element(*Locators.MailDraftPage.OVERLAY_SEARCH_TEXTBOX)
        self.send_keys(SearchTextBox, contact_name)
        time.sleep(1)

    def verify_search_contact_results_add_participant(self, contact_name):
        # AddParticipantDialog = self.get_element(Locators.MailDraftPage.ADD_PARTICIPANT_DIALOG)
        # SearchTextBox = AddParticipantDialog.find_element(*Locators.MailDraftPage.SEARCH_CONTACT_TEXT_BOX)
        # Overlay Code
        AddParticipantDialog = self.get_element(Locators.MailDraftPage.OVERLAY_DIALOG)
        SearchTextBox = AddParticipantDialog.find_element(*Locators.MailDraftPage.OVERLAY_SEARCH_TEXTBOX)
        self.send_keys(SearchTextBox, contact_name)
        time.sleep(1)
        Check = self.verify_contact_selection_dialog(contact_name)
        if Check:
            return True

    def verify_contact_name_added_field(self, contact_name):
        ToCcBccField = self.get_element(Locators.MailDraftPage.DRAFT_TO_CC_BCC_FIELD)
        ContactNameText = ToCcBccField.find_element(*Locators.MailDraftPage.CONTACT_LIST_OVERLAY).text
        if contact_name == ContactNameText:
            print(contact_name + "- Contact Added in Field")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_TO_CC_BCC_FIELD, "ContactAddedInField",
                                              "Verify Contact Added in Field")
            return True
        else:
            print(contact_name + "- Contact not Added in Field")
            self.screenshot_and_attach_report(Locators.MailDraftPage.CLARITI_FULL_VIEW, "ContactAddedInField",
                                              "Verify Contact Added in Field")
            return False

    def remove_added_contact(self):
        try:
            ToCcBccField = self.get_element(Locators.MailDraftPage.DRAFT_TO_CC_BCC_FIELD)
            RemoveIcon = ToCcBccField.find_element(*Locators.MailDraftPage.REMOVE_CONTACT_ICON)
            if RemoveIcon.is_displayed():
                RemoveIcon.click()
                time.sleep(0.5)
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_TO_CC_BCC_FIELD, "ContactRemovedInField",
                                                  "Verify Contact Removed in Field")
                return True
        except:
            print("Remove Icon not Displayed")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "ContactRemovedInField",
                                              "Verify Contact Removed in Field")
            return False

    def verify_file_explorer_opened(self):
        AttachIconArea = self.get_element(Locators.MailDraftPage.DRAFT_CC_BCC_ATTACHMENT_ICON_AREA)
        AttachIconArea.find_element(*Locators.MailDraftPage.DRAFT_ATTACHMENT_ICON).click()
        FileExplorerWindow = wait_for_file_explorer_open(15)
        if FileExplorerWindow:
            print("File Explorer is open.")
            print("File Explorer Title:", FileExplorerWindow.title)
            time.sleep(1)
            screenshot_and_attach_report_pyautogui("FileExplorerOpenedFromDraft",
                                                   "Verify File Explorer window will opened from Mail Draft")
            return True
        else:
            print("File Explorer did not open within the specified timeout.")
            screenshot_and_attach_report_pyautogui("FileExplorerNotOpenedFromDraft",
                                                   "Verify File Explorer window will opened from Mail Draft")
            return False

    def verify_max_10_files_alert(self):
        try:
            Alert = self.get_element(Locators.MailDraftPage.MAXIMUM_10_FILES_ALERT)
            if Alert:
                print("Alert Appears")
                Alert_Icon = self.get_element(Locators.MailDraftPage.MAXIMUM_10_FILES_ALERT_INFO_ICON)
                action = ActionChains(self.driver)
                action.move_to_element(Alert_Icon).perform()
                # screenshot_and_attach_report_pyautogui("Maximum10FilesAlert",
                #                                        "Verify Alert appears when upload more than 10 files")
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "Maximum10FilesAlert",
                                                  "Verify Alert appears when upload more than 10 files")
                return True
        except NoSuchElementException:
            print("Fail")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "Maximum10FilesAlert",
                                              "Verify Alert appears when upload more than 10 files")
            return False

    def remove_file_attachment(self, file_name):
        FileAttachmentsArea = self.get_element(Locators.MailDraftPage.FILE_ATTACHMENT_AREA)
        self.wait_for_element(Locators.MailDraftPage.FILE_ATTACHMENTS)
        File = FileAttachmentsArea.find_elements(*Locators.MailDraftPage.FILE_ATTACHMENTS)
        self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "BeforeRemovingAttachments",
                                          "Verify File Attachments Before Removing in Draft")
        if len(File) > 0:
            for eachFile in File:
                FileName = eachFile.find_element(*Locators.MailDraftPage.FILE_ATTACHMENT_NAME).text
                print(FileName)
                if FileName == file_name:
                    eachFile.find_element(*Locators.MailDraftPage.FILE_ATTACHMENT_DELETE_ICON).click()
                    self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "Maximum10FilesAlert",
                                                      "Verify File Attachments After Removed in Draft")
                    return True
        if len(File) == 0:
            print("File Attachments not found")
            return False

    def verify_file_attachment_added(self):
        FileAttachmentsArea = self.get_element(Locators.MailDraftPage.FILE_ATTACHMENT_AREA)
        self.wait_for_element(Locators.MailDraftPage.FILE_ATTACHMENTS)
        File = FileAttachmentsArea.find_elements(*Locators.MailDraftPage.FILE_ATTACHMENTS)
        if len(File) > 0:
            for eachFile in File:
                FileName = eachFile.find_element(*Locators.MailDraftPage.FILE_ATTACHMENT_NAME).text
                print(FileName)
                print("File Attachments found")
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "AttachmentsAdded",
                                                  "Verify File Attachments are Added")
            return True
        if len(File) == 0:
            print("File Attachments not found")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "AttachmentsNotAdded",
                                              "Verify File Attachments are Added")
            return False

    def verify_file_attachment_added_icons(self):
        FileAttachmentsArea = self.get_element(Locators.MailDraftPage.FILE_ATTACHMENT_AREA)
        self.wait_for_element(Locators.MailDraftPage.FILE_ATTACHMENTS)
        File = FileAttachmentsArea.find_elements(*Locators.MailDraftPage.FILE_ATTACHMENTS)
        if len(File) > 0:
            for eachFile in File:
                eachFile.find_element(*Locators.MailDraftPage.FILE_ATTACHMENT_SVG_ICON)
                print("File Attachments found with icon")
                self.screenshot_and_attach_report(Locators.MailDraftPage.FILE_ATTACHMENT_AREA, "FileAttachmentsArea",
                                                  "Verify File Attachments are Added with Icons")
            return True
        if len(File) == 0:
            print("File Attachments not found")
            self.screenshot_and_attach_report(Locators.MailDraftPage.FILE_ATTACHMENT_AREA, "AttachmentsNotAdded",
                                              "Verify File Attachments are Added with Icons")
            return False

    def cancel_uploading_files(self):
        FileAttachmentsArea = self.get_element(Locators.MailDraftPage.FILE_ATTACHMENT_AREA)
        self.wait_for_element(Locators.MailDraftPage.FILE_ATTACHMENTS)
        File = FileAttachmentsArea.find_elements(*Locators.MailDraftPage.FILE_ATTACHMENTS)
        self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "BeforeCancelUploadAttachments",
                                          "Verify File Attachments are Uploading")
        if len(File) > 0:
            for eachFile in File:
                eachFile.find_element(*Locators.MailDraftPage.FILE_ATTACHMENT_CANCEL_UPLOAD).click()
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "AfterCancelUploadAttachments",
                                                  "Verify File Attachments are cancelled while Uploading")
            return True
        if len(File) == 0:
            print("File Attachments not found")
            self.screenshot_and_attach_report(Locators.MailDraftPage.FILE_ATTACHMENT_AREA, "AttachmentsNotAdded",
                                              "Verify File Attachments are Added with Icons")
            return False

    def verify_show_editor_toolbar_displayed(self):
        DraftBody = self.get_element(Locators.MailDraftPage.MAIL_DRAFT_BODY)
        actions = ActionChains(self.driver)
        actions.move_to_element(DraftBody).perform()
        time.sleep(1)
        Icon = self.get_element(Locators.MailDraftPage.SHOW_EDITOR_TOOLBAR_ICON)
        actions.move_to_element(Icon).perform()
        Overlay = self.get_element(Locators.MailDraftPage.OVERLAY_CONTAINER)
        Tooltip = Overlay.find_element(*Locators.MailDraftPage.OVERLAY_TOOLTIP).text
        if Tooltip == "Show editor toolbar" or Icon:
            print("Show Editor Toolbar Icon appears and Tooltip appears")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "ShowEditorToolbarIcon ",
                                              "Verify Show Editor Toolbar Icon Displayed")
            return True
        else:
            print("Show Editor Toolbar Icon not appears and Tooltip not appears")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "ShowEditorToolbarIcon",
                                              "Verify Show Editor Toolbar Icon Displayed")
            return False

    def verify_editor_toolbar_opened(self):
        try:
            self.click_show_editor_toolbar_icon()
            time.sleep(1)
            Toolbar = self.get_element(Locators.MailDraftPage.EDITOR_TOOLBAR)
            if Toolbar:
                self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorToolbar",
                                                  "Verify Editor Toolbar Displayed")
                return True
        except NoSuchElementException:
            print("Editor Toolbar Not Opened")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorToolbar",
                                              "Verify Editor Toolbar Displayed or not")
            return False

    def verify_all_editor_action_hover_clickable(self):
        try:
            # Font Name
            self.click_editor_font_name()
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorFontName",
                                              "Verify Editor Font Name Dialog Displayed")
            self.click_to_close_dialog_overlay()
            time.sleep(0.5)

            # Font Size
            self.click_editor_font_size()
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorFontSize",
                                              "Verify Editor Font Size Dialog Displayed")
            self.click_to_close_dialog_overlay()
            time.sleep(0.5)

            # Bold
            actions = ActionChains(self.driver)
            Bold = self.get_element(Locators.MailDraftPage.EDITOR_TOOL_BOLD)
            actions.move_to_element(Bold).perform()
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorBoldHover",
                                              "Verify Editor Bold Button Hover and Tooltip Displayed")
            self.click_editor_bold()
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorBold",
                                              "Verify Editor Bold Button Clicked")
            time.sleep(0.5)

            # Italic
            actions = ActionChains(self.driver)
            Italic = self.get_element(Locators.MailDraftPage.EDITOR_TOOL_ITALIC)
            actions.move_to_element(Italic).perform()
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorItalicHover",
                                              "Verify Editor Italic Button Hover and Tooltip Displayed")
            self.click_editor_italic()
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorItalic",
                                              "Verify Editor Italic Button Clicked")
            time.sleep(0.5)

            # Strike Through
            actions = ActionChains(self.driver)
            StrikeThrough = self.get_element(Locators.MailDraftPage.EDITOR_TOOL_STRIKE)
            actions.move_to_element(StrikeThrough).perform()
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorStrikeThroughHover",
                                              "Verify Editor StrikeThrough Button Hover and Tooltip Displayed")
            self.click_editor_strike_through()
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorStrikeThrough",
                                              "Verify Editor StrikeThrough Button Clicked")
            time.sleep(0.5)

            # underline
            actions = ActionChains(self.driver)
            UnderLine = self.get_element(Locators.MailDraftPage.EDITOR_TOOL_UNDER_LINE)
            actions.move_to_element(UnderLine).perform()
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorUnderLineHover",
                                              "Verify Editor UnderLine Button Hover and Tooltip Displayed")
            self.click_editor_underline()
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorUnderLine",
                                              "Verify Editor UnderLine Button Clicked")
            time.sleep(0.5)

            # Left Align
            actions = ActionChains(self.driver)
            LeftAlign = self.get_element(Locators.MailDraftPage.EDITOR_TOOL_LEFT_ALIGN)
            actions.move_to_element(LeftAlign).perform()
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorLeftAlignHover",
                                              "Verify Editor LeftAlign Button Hover and Tooltip Displayed")
            self.click_editor_left_align()
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorLeftAlign",
                                              "Verify Editor LeftAlign Button Clicked")
            time.sleep(0.5)

            # Right Align
            actions = ActionChains(self.driver)
            RightAlign = self.get_element(Locators.MailDraftPage.EDITOR_TOOL_RIGHT_ALIGN)
            actions.move_to_element(RightAlign).perform()
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorRightAlignHover",
                                              "Verify Editor RightAlign Button Hover and Tooltip Displayed")
            self.click_editor_right_align()
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorRightAlign",
                                              "Verify Editor RightAlign Button Clicked")
            time.sleep(0.5)

            # Center Align
            actions = ActionChains(self.driver)
            CenterAlign = self.get_element(Locators.MailDraftPage.EDITOR_TOOL_CENTER_ALIGN)
            actions.move_to_element(CenterAlign).perform()
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorCenterAlignnHover",
                                              "Verify Editor CenterAlign Button Hover and Tooltip Displayed")
            self.click_editor_center_align()
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorCenterAlign",
                                              "Verify Editor CenterAlign Button Clicked")
            time.sleep(0.5)

            # Colour
            self.click_editor_colour()
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorPickColour",
                                              "Verify Editor Pick Colour Dialog Displayed")
            self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
            time.sleep(0.5)

            # Bullet List
            actions = ActionChains(self.driver)
            BulletList = self.get_element(Locators.MailDraftPage.EDITOR_TOOL_BULLET_LIST)
            actions.move_to_element(BulletList).perform()
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorBulletListHover",
                                              "Verify Editor BulletList Button Hover and Tooltip Displayed")
            self.click_editor_bullet_list()
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorBulletList",
                                              "Verify Editor BulletList Button Clicked")
            time.sleep(0.5)

            # Numbered List
            actions = ActionChains(self.driver)
            NumberedList = self.get_element(Locators.MailDraftPage.EDITOR_TOOL_NUMBER_LIST)
            actions.move_to_element(NumberedList).perform()
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorNumberedListHover",
                                              "Verify Editor NumberedList Button Hover and Tooltip Displayed")
            self.click_editor_numbered_list()
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorNumberedList",
                                              "Verify Editor NumberedList Button Clicked")
            time.sleep(0.5)

            # Indent
            actions = ActionChains(self.driver)
            Indent = self.get_element(Locators.MailDraftPage.EDITOR_TOOL_INDENT)
            actions.move_to_element(Indent).perform()
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorIndentHover",
                                              "Verify Editor Indent Button Hover and Tooltip Displayed")
            self.click_editor_indent()
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorIndent",
                                              "Verify Editor Indent Button Clicked")
            time.sleep(0.5)

            # Reduce indent
            actions = ActionChains(self.driver)
            ReduceIndent = self.get_element(Locators.MailDraftPage.EDITOR_TOOL_REDUCE_INDENT)
            actions.move_to_element(ReduceIndent).perform()
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorReduceIndentHover",
                                              "Verify Editor ReduceIndent Button Hover and Tooltip Displayed")
            self.click_editor_reduce_indent()
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorReduceIndent",
                                              "Verify Editor ReduceIndent Button Clicked")
            time.sleep(0.5)

            # More Icon
            actions = ActionChains(self.driver)
            MoreIcon = self.get_element(Locators.MailDraftPage.EDITOR_TOOL_MORE_ICON)
            actions.move_to_element(MoreIcon).perform()
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorMoreIconHover",
                                              "Verify Editor More Button Hover and Tooltip Displayed")
            self.click_editor_more_icon()
            time.sleep(1)
            Overlay = self.get_element(Locators.MailDraftPage.OVERLAY_CONTAINER)
            draft_body_text = Overlay.find_element(*Locators.MailDraftPage.OVERLAY_ACTION_CLASS)
            actions = draft_body_text.find_elements(*Locators.MailDraftPage.BUTTON_TAG)
            print(len(actions))
            if len(actions) == 3:
                print("3 Options are there")
            elif len(actions) == 3:
                print("4 Options are there")
            else:
                print("Options are not showing")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorMoreIcon",
                                              "Verify Editor MoreIcon Button Clicked")
            self.click_to_close_dialog_overlay()
            time.sleep(0.5)
            return True
        except NoSuchElementException:
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "OneOfTheActionHaveProblem",
                                              "Any One of the Action is problem in editor toolbar")
            return False

    def verify_font_size_click(self):
        self.click_editor_font_size()
        time.sleep(1)
        self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "EditorFontSize",
                                          "Verify Editor Font Size Dialog Displayed")

    def verify_body_draft_text_style_bold(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_BOLD)
        time.sleep(1)
        try:
            if DraftBody.find_element(*Locators.MailDraftPage.BOLD_TAG):
                print("Entered text changed to BOLD")
                self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
                self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoBold",
                                                  "Verify Entered Text Changed to Bold")

                return True
        except NoSuchElementException:
            print("Entered text not changed to BOLD")
            self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoBold",
                                              "Verify Entered Text Changed to Bold or not")
            return False

    def click_disable_bold(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_BOLD)

    def verify_body_draft_text_style_italic(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_ITALIC)
        time.sleep(1)
        try:
            if DraftBody.find_element(*Locators.MailDraftPage.ITALIC_TAG):
                print("Entered text changed to Italic")
                self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoItalic",
                                                  "Verify Entered Text Changed to Italic")

                return True
        except NoSuchElementException:
            print("Entered text not changed to Italic")
            self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoItalic",
                                              "Verify Entered Text Changed to Italic or not")
            return False

    def click_disable_italic(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_ITALIC)

    def verify_body_draft_text_style_strike_through(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_STRIKE)
        time.sleep(1)
        try:
            if DraftBody.find_element(*Locators.MailDraftPage.STRIKE_TAG):
                print("Entered text changed to Strike")
                self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
                self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoStrike",
                                                  "Verify Entered Text Changed to Strike")

                return True
        except NoSuchElementException:
            print("Entered text not changed to Strike")
            self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoStrike",
                                              "Verify Entered Text Changed to Strike or not")
            return False

    def click_disable_strike(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_STRIKE)

    def verify_body_draft_text_style_under_line(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_UNDER_LINE)
        time.sleep(1)
        try:
            if DraftBody.find_element(*Locators.MailDraftPage.UNDER_LINE_TAG):
                print("Entered text changed to UnderLine")
                self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
                self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoUnderLine",
                                                  "Verify Entered Text Changed to UnderLine")

                return True
        except NoSuchElementException:
            print("Entered text not changed to UnderLine")
            self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoUnderLine",
                                              "Verify Entered Text Changed to UnderLine or not")
            return False

    def click_disable_under_line(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_UNDER_LINE)

    def verify_body_draft_text_style_bullet_list(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_BULLET_LIST)
        time.sleep(1)
        try:
            if DraftBody.find_element(*Locators.MailDraftPage.BULLET_LIST_TAG):
                print("Entered text changed to BulletList")
                self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
                self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoBulletList",
                                                  "Verify Entered Text Changed to BulletList")

                return True
        except NoSuchElementException:
            print("Entered text not changed to BulletList")
            self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoBulletList",
                                              "Verify Entered Text Changed to BulletList or not")
            return False

    def click_disable_bullet_list(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_BULLET_LIST)

    def verify_body_draft_text_style_numbered_list(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_NUMBER_LIST)
        time.sleep(1)
        try:
            if DraftBody.find_element(*Locators.MailDraftPage.NUMBERED_LIST_TAG):
                print("Entered text changed to NumberedList")
                self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
                self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoNumberedList",
                                                  "Verify Entered Text Changed to NumberedList")

                return True
        except NoSuchElementException:
            print("Entered text not changed to NumberedList")
            self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoNumberedList",
                                              "Verify Entered Text Changed to NumberedList or not")
            return False

    def click_disable_numbered_list(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_NUMBER_LIST)

    def verify_body_draft_text_style_indent(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        DraftBodyMain = self.get_element(Locators.MailDraftPage.DRAFT_BODY)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_INDENT)
        time.sleep(1)
        try:
            if DraftBodyMain.find_element(*Locators.MailDraftPage.INDENT_TAG):
                print("Entered text changed to Indent")
                self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
                self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoIndent",
                                                  "Verify Entered Text Changed to Indent")

                return True
        except NoSuchElementException:
            print("Entered text not changed to Indent")
            self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoIndent",
                                              "Verify Entered Text Changed to Indent or not")
            return False

    def click_disable_indent(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_INDENT)

    def verify_body_draft_text_style_reduce_indent(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        DraftBodyMain = self.get_element(Locators.MailDraftPage.DRAFT_BODY)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_REDUCE_INDENT)
        time.sleep(1)
        try:
            if DraftBodyMain.find_element(*Locators.MailDraftPage.INDENT_TAG):
                print("Entered text not changed to Reduce Indent")
                self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
                self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoReduceIndent",
                                                  "Verify Entered Text Changed to ReduceIndent or not,.")

                return False
        except NoSuchElementException:
            print("Entered text changed to ReduceIndent")
            self.click(Locators.MailDraftPage.DRAFT_BODY_TEXT)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoReduceIndent",
                                              "Verify Entered Text Changed to ReduceIndent")
            return True

    def verify_body_draft_text_style_center(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_CENTER_ALIGN)
        time.sleep(1)
        computed_style = DraftBody.value_of_css_property('text-align')
        # Verify if the text alignment is set to "center"
        if computed_style == 'center':
            print("Text alignment is center")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoCenter",
                                              "Verify Entered Text Changed to Center")
            return True

        else:
            print(f"Text alignment is {computed_style}")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoCenter",
                                              "Verify Entered Text not Changed to Center")
            return False

    def verify_body_draft_text_style_right(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_RIGHT_ALIGN)
        time.sleep(1)
        computed_style = DraftBody.value_of_css_property('text-align')
        # Verify if the text alignment is set to "Right"
        if computed_style == 'right':
            print("Text alignment is right")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoright",
                                              "Verify Entered Text Changed to right")
            return True

        else:
            print(f"Text alignment is {computed_style}")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoright",
                                              "Verify Entered Text not Changed to right")
            return False

    def verify_body_draft_text_style_left(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        self.click(Locators.MailDraftPage.EDITOR_TOOL_LEFT_ALIGN)
        time.sleep(1)
        computed_style = DraftBody.value_of_css_property('text-align')
        # Verify if the text alignment is set to "left"
        if computed_style == 'left':
            print("Text alignment is left")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoleft",
                                              "Verify Entered Text Changed to left")
            return True

        else:
            print(f"Text alignment is {computed_style}")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextChangedtoleft",
                                              "Verify Entered Text not Changed to left")
            return False

    def verify_body_draft_text_style_colour(self):
        DraftBody = self.get_element(Locators.MailDraftPage.DRAFT_BODY_TEXT)
        actions = ActionChains(self.driver)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.click(DraftBody)
        actions.perform()
        font_colour = self.get_element(Locators.MailDraftPage.EDITOR_TOOL_COLOUR)
        self.click(Locators.MailDraftPage.EDITOR_TOOL_COLOUR)
        time.sleep(1)
        Colour_tool = font_colour.find_element(*Locators.MailDraftPage.EDITOR_TOOL_COLOUR_LIST_DIALOG)
        AllColours = Colour_tool.find_elements(*Locators.MailDraftPage.EDITOR_TOOL_COLOUR_LIST)
        random_color = random.choice(AllColours)
        color_element = random_color.find_element(*Locators.MailDraftPage.EDITOR_TOOL_COLOUR_LIST_ITEM)
        color_class = color_element.get_attribute("class")
        print(color_class)
        Colour = color_class.split("im-da-dr-draftToolBarFont")[-1]
        print("Selected Colour: " + Colour)
        color_element.click()
        colour_icon = self.get_element(Locators.MailDraftPage.EDITOR_TOOL_COLOUR_ICON)
        style_attribute = colour_icon.get_attribute("style")
        background_color = style_attribute.split("background-color:")[1].strip().strip(";")
        rgb_values = re.findall(r'\d+', background_color)

        # Convert the RGB values to hexadecimal
        hex_color = "#{:02X}{:02X}{:02X}".format(int(rgb_values[0]), int(rgb_values[1]), int(rgb_values[2]))

        font_element = DraftBody.find_element(By.XPATH, ".//font")

        # Get the value of the color attribute
        color_attribute = font_element.get_attribute("color")

        DraftBody.click()
        if hex_color.lower() == color_attribute.lower():
            print("Text Colour is changed to random")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextColourChanged",
                                              "Verify Entered Text Colour Changed to - " + Colour)
            return True

        else:
            print("Text Colour is not changed to random")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "TextColourChanged",
                                              "Verify Entered Text Colour Changed to - " + Colour)
            return False

    def insert_image_in_draft(self):
        self.click_editor_insert_image()
        wait_for_file_explorer_open(15)
        upload_files("one", "S_image.jpg", "")
        self.wait_for_element(Locators.MailDraftPage.IMAGE_TAG)

    def verify_insert_image_in_draft(self):
        self.insert_image_in_draft()
        time.sleep(1)
        draft_body_area = self.get_element(Locators.MailDraftPage.DRAFT_BODY)
        try:
            draft_body_area.find_element(*Locators.MailDraftPage.IMAGE_TAG)
            print("Inline Added")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "InlineImageAdded",
                                              "Verify Inline Image Added In Draft")
            return True
        except NoSuchElementException:
            print("Inline Not Added")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "InlineImageNotAdded",
                                              "Verify Inline Image Added In Draft")
            return False

    def verify_insert_image_is_clickable(self):
        draft_body_area = self.get_element(Locators.MailDraftPage.DRAFT_BODY)
        try:
            Image_Tag = draft_body_area.find_element(*Locators.MailDraftPage.IMAGE_TAG)
            Image_Tag.click()
            time.sleep(1)
            style_attribute = Image_Tag.get_attribute("style")
            if "border: 2px solid red" in style_attribute:
                self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "InlineImageSelected",
                                                  "Verify Inline Image Clickable and Selection in Inline In Draft")
                return True
            else:
                print("Border not appears and Image not selected")
                self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "InlineImageNotSelected",
                                                  "Verify Inline Image Clickable and Selection in Inline In Draft")
                return False
        except NoSuchElementException:
            print("Inline Not Added")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "InlineImageNotAdded",
                                              "Verify Inline Image Added In Draft")
            return False

    def verify_resize_insert_image_in_draft(self):
        self.insert_image_in_draft()
        time.sleep(1)
        draft_body_area = self.get_element(Locators.MailDraftPage.DRAFT_BODY)
        try:
            Image_Tag = draft_body_area.find_element(*Locators.MailDraftPage.IMAGE_TAG)
            Image_Tag.click()
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "InlineImageBeforeResize",
                                              "Verify Inline Image Before Resize In Draft")
            self.driver.execute_script("arguments[0].style.width='120px'; arguments[0].style.height='120px';", Image_Tag)
            time.sleep(1)
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "InlineImageAfterResize",
                                              "Verify Inline Image After Resize In Draft")
            return True
        except NoSuchElementException:
            print("Inline Not Resized")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "InlineImageNotAddedOrResized",
                                              "Verify Inline Image Resized In Draft")
            return False

    def verify_delete_backspace_operation_inline_image(self, key):
        self.insert_image_in_draft()
        time.sleep(1)
        draft_body_area = self.get_element(Locators.MailDraftPage.DRAFT_BODY)
        try:
            Image_Tag = draft_body_area.find_element(*Locators.MailDraftPage.IMAGE_TAG)
            Image_Tag.click()
            time.sleep(1)
            if key == "delete":
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.DELETE).perform()
                time.sleep(1)
                try:
                    if draft_body_area.find_element(*Locators.MailDraftPage.IMAGE_TAG):
                        print("Image not Deleted when using DELETE Key")
                        self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "InlineImagenNotDeleted",
                                                          "Verify Inline Image Not Deleted Using DELETE Key In Draft")
                        return True
                except NoSuchElementException:
                    print("Image Deleted when using DELETE Key")
                    self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "InlineImagenNotDeleted",
                                                      "Verify Inline Image Not Deleted Using DELETE Key In Draft")
                    return False
            elif key == "backspace":
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.BACKSPACE).perform()
                time.sleep(1)
                try:
                    if draft_body_area.find_element(*Locators.MailDraftPage.IMAGE_TAG):
                        print("Image not Deleted when using BACKSPACE Key")
                        self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "InlineImageDeleted",
                                                          "Verify Inline Image Not Deleted Using BACKSPACE Key In Draft")
                        return False
                except NoSuchElementException:
                    print("Image Deleted when using BACKSPACE Key")
                    self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "InlineImageDeleted",
                                                      "Verify Inline Image Not Deleted Using BACKSPACE Key In Draft")
                    return True
            else:
                print("Enter a Valid Key: " + key)
                return False
        except NoSuchElementException:
            print("Fail")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_BODY, "InlineImageNotAdded",
                                              "Verify Inline Image Added In Draft")
            return False

    def verify_hyperlink_dialog_opened(self):
        self.click_editor_insert_hyperlink()
        self.wait_for_element(Locators.MailDraftPage.HYPERLINK_DIALOG)
        if Locators.MailDraftPage.HYPERLINK_DIALOG:
            print("Hyperlink Opened")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "HyperlinkDialogOpened",
                                              "Verify Hyperlink Dialog Opened or Not")
            return True
        else:
            print("Hyperlink Not Opened")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "HyperlinkDialogNotOpened",
                                              "Verify Hyperlink Dialog Opened or Not")
            return False

    def verify_hyperlink_dialog_Text_to_be_displayed_textbox_focused(self):
        try:
            text_box = self.get_element(Locators.MailDraftPage.FOCUSED_TEXTBOX_HYPERLINK)
            if text_box:
                print("The text box is the currently active element")
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "CursorTextBoxFocused",
                                                  "Cursor is focused in Text to be displayed Field and its active")
                return True

        except NoSuchElementException:
            print("The text box is not the currently active element")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "CursorTextBoxNotFocused",
                                              "Cursor is not focused in Text to be displayed Field and its not active")
            return False

    def enter_hyperlink_text(self, text_to_be_displayed):
        self.send_keys(Locators.MailDraftPage.HYPERLINK_URL_TEXT_TEXTBOX, text_to_be_displayed)

    def verify_hyperlink_text_to_be_displayed(self, text_to_be_displayed):
        self.enter_hyperlink_text(text_to_be_displayed)
        time.sleep(0.5)
        try:
            text_box = self.get_element(Locators.MailDraftPage.FOCUSED_TEXTBOX_HYPERLINK)
            if text_box:
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "HyperlinkTextToBeDisplayedText", "Verify Text entered in Text to be displayed Field")
                return True
        except NoSuchElementException:
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "HyperlinkTextToBeDisplayedTextNotDisplayed",
                                              "Verify Text entered in Text to be displayed Field")

            return False

    def enter_hyperlink_url(self, url_text):
        self.send_keys(Locators.MailDraftPage.HYPERLINK_URL_TEXTBOX, url_text)

    def verify_hyperlink_url(self, url_text):
        self.enter_hyperlink_url(url_text)
        time.sleep(0.5)
        try:
            text_box = self.get_element(Locators.MailDraftPage.FOCUSED_TEXTBOX_HYPERLINK)
            if text_box:
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "HyperlinkUrlText", "Verify URL entered in url Field")
                return True
        except NoSuchElementException:
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "HyperlinkUrlTextNotDisplayed", "Verify URL entered in url Field")
            return False

    def verify_insert_button_enabled(self):
        insert_button = self.get_element(Locators.MailDraftPage.HYPERLINK_INSERT_BUTTON)
        if insert_button.is_enabled():
            print("Enabled")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "InsertButtonEnabled", "Verify Insert Button Enabled")
            return True
        else:
            print("Disabled")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "InsertButtonDisabled", "Verify Insert Button Enabled or Disabled")
            return False

    def verify_insert_button_disabled(self):
        insert_button = self.get_element(Locators.MailDraftPage.HYPERLINK_INSERT_BUTTON)
        if not insert_button.is_enabled():
            print("Disabled")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "InsertOrSaveButtonDisabled", "Verify Insert/Save Button Disabled")
            return True
        else:
            print("Enabled")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "InsertOrSaveButtonDisabled", "Verify Insert/Save Button Enabled or Disabled")
            return False

    def verify_hyperlink_preview_text(self):
        try:
            Preview = self.get_element(Locators.MailDraftPage.HYPERLINK_PREVIEW_LINK)
            if Preview.is_enabled():
                print("Hyperlink Preview Appears")
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "HyperlinkPreviewAppears",
                                                  "Verify Hyperlink Preview Appears")
                return True

        except NoSuchElementException:
            print("Hyperlink Preview Not Appears")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "HyperlinkPreviewNotAppears", "Verify Hyperlink Preview Appears or Not")
            return False

    def click_hyperlink_preview(self):
        self.click(Locators.MailDraftPage.HYPERLINK_PREVIEW_LINK)

    def verify_hyperlink_clicked_new_tab(self):
        try:
            self.click_hyperlink_preview()
            time.sleep(1)
            All_Windows = self.driver.window_handles
            if len(All_Windows) > 1:
                self.driver.switch_to.window(All_Windows[1])
                wait = WebDriverWait(self.driver, 10)

                # Wait until the page is fully loaded (wait for the presence of the body tag)
                wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                screenshot_and_attach_report_pyautogui("MoreThan1Tab", "Verify New tab opened after clicking hyperlink")
                time.sleep(1)
                self.driver.close()
                self.driver.switch_to.window(All_Windows[0])
                return True
            else:
                print("Only 1 tab is opened or newly clicked link is not opened")
                screenshot_and_attach_report_pyautogui("MoreThan1Tab", "Verify New tab opened after clicking hyperlink")
                self.driver.switch_to.window(All_Windows[0])
                return False

        except NoSuchElementException:
            print("Hyperlink Preview Not Appears")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "HyperlinkPreviewNotAppears", "Verify Hyperlink Preview Appears or Not")
            return False

    def verify_not_a_valid_url_alert(self):
        try:
            Hyperlink_dialog = self.get_element(Locators.MailDraftPage.HYPERLINK_DIALOG)
            Alert = Hyperlink_dialog.find_element(*Locators.MailDraftPage.HYPERLINK_ERROR_NOT_A_VALID_URL)
            if Alert.text == "Not a valid Url":
                print("Not a Valid URL Alert Appears")
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "NotAValidUrlAlert",
                                                  "Verify Not a valid URL alert appears")
                return True
        except NoSuchElementException:
            print("Not a Valid URL Alert not Appears")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "NotAValidUrlAlertNotAppears",
                                              "Verify Not a valid URL alert")
            return False

    def click_close_icon_hyperlink(self):
        close_icon = self.get_element(Locators.MailDraftPage.HYPERLINK_DIALOG)
        Close = close_icon.find_element(*Locators.MailDraftPage.HYPERLINK_DIALOG_CLOSE)
        Close.click()

    def clear_entered_text_text_to_be_displayed(self):
        try:
            text_box = self.get_element(Locators.MailDraftPage.HYPERLINK_URL_TEXT_TEXTBOX)
            text_box.click()
            actions = ActionChains(self.driver)
            actions.click(text_box)
            actions.click(text_box)
            actions.click(text_box)
            actions.perform()
            actions.send_keys(Keys.BACKSPACE).perform()
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "HyperlinkTextToBeDisplayedTextCleared",
                                              "Verify Text entered in Text to be displayed Field is cleared")

            return True
        except NoSuchElementException:
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "HyperlinkTextToBeDisplayedTextCleared",
                                              "Verify Text entered in Text to be displayed Field is cleared")
            return False

    def verify_signature_dialog_opened(self):
        self.click_editor_signature()
        #self.wait_for_element(Locators.MailDraftPage.SIGNATURE_DIALOG)
        SignatureDialog = self.get_element(Locators.MailDraftPage.SIGNATURE_DIALOG)
        if SignatureDialog.is_displayed():
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "SignatureDialogOpened",
                                              "Verify Signature Dialog Opened")
            return True
        else:
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "SignatureDialogOpened",
                                              "Verify Signature Dialog Opened")
            return False

    def verify_default_signature(self):
        self.click_editor_signature()
        time.sleep(1)
        #self.wait_for_element(Locators.MailDraftPage.SIGNATURE_DIALOG)
        DefaultText = self.get_text(Locators.MailDraftPage.BODY_AREA)
        print(DefaultText)
        if "Sent using Clariti" in DefaultText:
            print("Text appears")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "DefaultSignature",
                                              "Verify Default Signature is showing in signature Dialog.")
            return True
        else:
            print("Text not appears")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "DefaultSignature",
                                              "Verify Default Signature is showing in signature Dialog.")
            return False

    def verify_add_this_signature_for_all_mails_enabled(self):
        CheckBoxArea = self.get_element(Locators.MailDraftPage.CHECKBOX_AREA)
        CheckBoxInput = CheckBoxArea.find_element(*Locators.MailDraftPage.CHECKBOX_INPUT)
        if CheckBoxInput.is_selected():
            print("Default Selection is enabled")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "DefaultSelectionEnabledSignature",
                                              "Verify Default Selection Enabled for all mails in signature Dialog.")
            return True
        else:
            print("Default Selection is not enabled")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "DefaultSelectionEnabledSignature",
                                              "Verify Default Selection Enabled for all mails in signature Dialog.")
            return False

    def uncheck_signature_for_all_mails(self):
        CheckBoxArea = self.get_element(Locators.MailDraftPage.CHECKBOX_AREA)
        CheckBoxInput = CheckBoxArea.find_element(*Locators.MailDraftPage.CHECKBOX_INPUT)
        CheckBoxArea.click()

    def verify_add_this_signature_for_all_mails_uncheck(self):
        CheckBoxArea = self.get_element(Locators.MailDraftPage.CHECKBOX_AREA)
        CheckBoxInput = CheckBoxArea.find_element(*Locators.MailDraftPage.CHECKBOX_INPUT)
        CheckBoxArea.click()
        if not CheckBoxInput.is_selected():
            print("Selection is disabled")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "SelectionDisabledSignature",
                                              "Verify Selection is Disabled for all mails in signature Dialog.")
            return True
        else:
            print("Selection is not disabled")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "SelectionDisabledSignature",
                                              "Verify Selection is Disabled for all mails in signature Dialog.")
            return False

    def click_Apply_button_signature(self):
        self.click(Locators.MailDraftPage.HYPERLINK_INSERT_BUTTON)

    def verify_signature_dialog_closed_apply(self):
        self.click(Locators.MailDraftPage.HYPERLINK_INSERT_BUTTON)
        self.wait_for_element_disappears(Locators.MailDraftPage.HYPERLINK_DIALOG)
        self.click(Locators.MailDraftPage.SUBJECT_FIELD)
        text_box = self.get_element(Locators.MailDraftPage.SUBJECT_FIELD)
        is_active_element = text_box == self.driver.switch_to.active_element
        if is_active_element:
            print("Signature Dialog closed after clicking Apply")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "SignatureDialogClosed",
                                              "Verify Signature Dialog closed after clicking Apply Button.")
            return True
        else:
            print("Signature Dialog is not closed after clicking Apply")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "SignatureDialogClosed",
                                              "Verify Signature Dialog closed after clicking Apply Button.")
            return False

    def change_default_signature_and_verify(self):
        DefaultText = self.get_text(Locators.MailDraftPage.BODY_AREA)
        print(DefaultText)
        self.send_keys(Locators.MailDraftPage.BODY_AREA, " "+random_string(5))
        ChangedText = self.get_text(Locators.MailDraftPage.BODY_AREA)
        print(ChangedText)
        self.uncheck_signature_for_all_mails()
        time.sleep(0.5)
        self.click_Apply_button_signature()
        UpdatedText = self.get_text(Locators.MailDraftPage.BODY_AREA)
        print(UpdatedText)
        if ChangedText in UpdatedText:
            print("Signature Changed")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "DefaultSignatureUpdated",
                                              "Verify Default Signature Changed to New One.")
            return True
        else:
            print("Signature Not Changed")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "DefaultSignatureNotUpdated",
                                              "Verify Default Signature Changed to New One.")
            return False

    # Current code until issue fix
    def clear_unwanted_signature(self):
        DefaultText = self.get_text(Locators.MailDraftPage.BODY_AREA)
        print(DefaultText)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.BACKSPACE).perform()
        actions.send_keys(Keys.BACKSPACE).perform()
        actions.send_keys(Keys.BACKSPACE).perform()
        actions.send_keys(Keys.BACKSPACE).perform()
        actions.send_keys(Keys.BACKSPACE).perform()
        actions.send_keys(Keys.BACKSPACE).perform()

    def verify_more_actions_in_signature_dialog(self):
        self.click_editor_more_icon()
        time.sleep(1)
        Overlay = self.get_element(Locators.MailDraftPage.OVERLAY_CONTAINER)
        draft_body_text = Overlay.find_element(*Locators.MailDraftPage.OVERLAY_ACTION_CLASS)
        actions = draft_body_text.find_elements(*Locators.MailDraftPage.BUTTON_TAG)
        print(len(actions))
        if len(actions) == 2:
            print("2 Options are there")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "EditorMoreIconSignatureDialog",
                                              "Verify Editor MoreIcon Button Clicked in Signature Dialog and 2 Options Should be Visible")
            self.click_to_close_dialog_overlay()
            time.sleep(0.5)
            return True

        else:
            print("Options are not showing")
            self.screenshot_and_attach_report(Locators.MailDraftPage.MAIL_DRAFT_LAYOUT, "EditorMoreIconSignatureDialog",
                                              "Verify Editor MoreIcon Button Clicked in Signature Dialog and 2 Options Should be Visible")
            self.click_to_close_dialog_overlay()
            time.sleep(0.5)
            return False

    def click_reply_to_option(self):
        self.click_editor_more_icon()
        time.sleep(0.5)
        overlay = self.get_element(Locators.MailDraftPage.OVERLAY_CONTAINER)
        overlay.find_element(*Locators.MailDraftPage.EDITOR_TOOL_REPLY_TO_OVERLAY).click()
        self.wait_for_element(Locators.MailDraftPage.HYPERLINK_DIALOG)

    def verify_reply_to_dialog_opened(self):
        self.click_reply_to_option()
        if Locators.MailDraftPage.HYPERLINK_DIALOG:
            print("Reply To Dialog Opened")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "ReplyToDialogOpened",
                                              "Verify Reply To Dialog Opened or Not")
            return True
        else:
            print("Reply To Dialog Not Opened")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "ReplyToDialogNotOpened",
                                              "Verify Reply To Dialog Opened or Not")
            return False

    def verify_enter_valid_email_address_alert_reply_to(self):
        # self.click_reply_to_option()
        self.send_keys(Locators.MailDraftPage.REPLY_TO_TEXTBOX, random_string(6))
        time.sleep(1)
        self.click(Locators.MailDraftPage.HYPERLINK_INSERT_BUTTON)
        try:
            ReplyTo_dialog = self.get_element(Locators.MailDraftPage.HYPERLINK_DIALOG)
            Alert = ReplyTo_dialog.find_element(*Locators.MailDraftPage.HYPERLINK_ERROR_NOT_A_VALID_URL)
            if Alert.text == "Enter valid mail address":
                print("Enter valid mail address Alert Appears")
                time.sleep(0.5)
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "EnterValidMailAddressAlert",
                                                  "Verify Enter valid mail address alert appears")
                return True
        except NoSuchElementException:
            print("Enter valid mail address Alert not Appears")
            time.sleep(0.5)
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "EnterValidMailAddressAlertNot",
                                              "Verify Enter valid mail address alert")
            return False

    def enter_email_address_alert_reply_to(self, reply_to_email):
        # self.click_reply_to_option()
        self.send_keys(Locators.MailDraftPage.REPLY_TO_TEXTBOX, reply_to_email)
        time.sleep(1)
        self.click(Locators.MailDraftPage.HYPERLINK_INSERT_BUTTON)
        time.sleep(1)

    def verify_reply_for_this_email_sent_to_email(self, reply_to_email):
        self.enter_email_address_alert_reply_to(reply_to_email)
        ReplyText = self.get_text(Locators.MailDraftPage.REPLY_TO_MSG_DRAFT)
        if Locators.MailDraftPage.REPLY_TO_MSG_DRAFT_LABEL_TEXT in ReplyText:
            if reply_to_email in ReplyText:
                print("Both Reply To label and Email id appears")
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "ReplyToEmailAppearInDraft",
                                                  "Verify Both Reply To label and Email id appears")
                return True
            else:
                print("Reply To Email id not appears")
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "ReplyToEmailNotAppearInDraft",
                                                  "Verify Both Reply To label and Email id appears")
                return False
        else:
            print("Both Reply To label and Email id not appears")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "ReplyToEmailLabelNotAppearInDraft",
                                              "Verify Both Reply To label and Email id appears")
            return False

    def clear_reply_to_email(self):
        ReplyToEmail = self.get_element(Locators.MailDraftPage.REPLY_TO_TEXTBOX)
        actions = ActionChains(self.driver)
        actions.click(ReplyToEmail)
        actions.click(ReplyToEmail)
        actions.click(ReplyToEmail)
        actions.perform()
        actions.send_keys(Keys.BACKSPACE).perform()
        time.sleep(0.5)
        self.click(Locators.MailDraftPage.HYPERLINK_INSERT_BUTTON)

    def verify_info_icon_alert_draft_both_messages(self, Alert):
        InfoIcon = self.get_element(Locators.MailDraftPage.SEND_INFO_DRAFT_AREA)
        actions = ActionChains(self.driver)
        actions.move_to_element(InfoIcon).perform()
        InfoMessage = self.get_element(Locators.MailDraftPage.INFO_MESSAGE_CLASS)
        inner_html = InfoMessage.get_attribute("innerHTML")
        soup = BeautifulSoup(inner_html, "html.parser")
        JoinMultiLineText = ' '.join(soup.stripped_strings)
        print(JoinMultiLineText)
        if Alert == "subject":
            if "Information: Subject is empty" in JoinMultiLineText:
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "SubjectEmptyInfWoMessageLabel",
                                                  "Verify Subject is Empty Info Message Appears")
                return True
            else:
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "SubjectEmptyInfoMessageLabel",
                                                  "Verify Subject is Empty Info Message Appears")
                return False
        if Alert == "recipient":
            if "Information: Atleast one recipient is required" in JoinMultiLineText:
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "RecipientRequiredInfoMessageLabel",
                                                  "Verify Recipient Required Info Message Appears")
                return True
            else:
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "RecipientRequiredInfoMessageLabel",
                                                  "Verify Recipient Required Info Message Appears")
                return False

        if Alert == "both":
            if "Information: Atleast one recipient is required Subject is empty" in JoinMultiLineText:
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "InfoMessageLabel",
                                                  "Verify Both Info Alert Appears")
                return True
            else:
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "InfoMessageLabel",
                                                  "Verify Both Info Alert Appears")
                return False

    def verify_send_button_disabled_state(self):
        try:
            button = self.get_element(Locators.MailDraftPage.MAT_BUTTON_DISABLED)

            # Check if the button is enabled or disabled
            if not button.is_enabled():
                print("Button is disabled.")
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "SendButtonDisabled",
                                                  "Verify Send Button Disabled")
                return True
        except NoSuchElementException:
            print("Button is enabled.")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "SendButtonEnabled",
                                              "Verify Send Button Enabled or Disabled")
            return False

    def verify_mail_will_be_sent_using(self):
        try:
            sent_using = self.get_element(Locators.MailDraftPage.MAIL_WILL_BE_SENT_USING)
            if sent_using.is_displayed():
                print("Sent using Enabled")
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "sentUsingEnabled",
                                                  "Verify mail will be sent using enabled")
                return True
        except NoSuchElementException:
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "sentUsingNotEnabled",
                                              "Verify mail will be sent using enabled")
            return False

    def verify_mail_will_be_sent_using_not_appears(self):
        try:
            sent_using = self.get_element(Locators.MailDraftPage.MAIL_WILL_BE_SENT_USING)
            if sent_using.is_displayed():
                print("Sent using Enabled")
                self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "sentUsingEnabled",
                                                  "Verify mail will be sent using not enabled")
                return False
        except NoSuchElementException:
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "sentUsingNotEnabled",
                                              "Verify mail will be sent using not enabled")
            return True

    def select_draft(self):
        Drafts = self.get_element(Locators.MailDraftPage.DRAFT_LAYOUT_CONTEXTS_AREA)
        print(len(Drafts))
        for eachDraft in Drafts:
            eachDraft.click()
            break

    def verify_click_mail_sent_using_dropdown(self):
        mail_sent_using_email_id = self.get_element(Locators.MailDraftPage.MAIL_WILL_BE_SENT_USING_EMAIL_ID)
        print(mail_sent_using_email_id.text)
        mail_sent_using_email_id.click()
        time.sleep(1)
        overlayPane = self.get_element(Locators.MailDraftPage.OVERLAY_PANE)
        if overlayPane.is_displayed():
            print("DropDown Appears for Sent using mail id")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "sentUsingDropdownClick",
                                              "Verify clicking Dropdown of Sent Using")
            return True
        else:
            print("DropDown Appears for Sent using mail id")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "sentUsingDropdownClick",
                                              "Verify clicking Dropdown of Sent Using")
            return False

    def click_mail_sent_using_dropdown(self):
        self.click(Locators.MailDraftPage.MAIL_WILL_BE_SENT_USING_EMAIL_ID)
        time.sleep(1)

    def verify_select_configured_mail_dropdown(self):
        mail_sent_using_email_id = self.get_element(Locators.MailDraftPage.MAIL_WILL_BE_SENT_USING_EMAIL_ID)
        print("Default sent using mail id:  "+mail_sent_using_email_id.text)
        #mail_sent_using_email_id.click()
        time.sleep(1)
        overlayPane = self.get_element(Locators.MailDraftPage.OVERLAY_PANE)
        EmailId = overlayPane.find_element(*Locators.MailDraftPage.MAIL_WILL_BE_SENT_USING_EMAIL_ID_DROP_DOWN)
        print("Configured another mail id:  "+EmailId.text)
        EmailIdText = EmailId.text
        EmailId.click()
        time.sleep(1)
        mail_sent_using_email_id = self.get_element(Locators.MailDraftPage.MAIL_WILL_BE_SENT_USING_EMAIL_ID)
        print("Changed sent using mail id:  "+mail_sent_using_email_id.text)
        if mail_sent_using_email_id.text == EmailIdText:
            print("Email ID Changed")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "sentUsingSelectEmail",
                                              "Verify select configured mail from mail will be sent using dropdown")
            return True
        else:
            print("Email ID Not Changed")
            self.screenshot_and_attach_report(Locators.MailDraftPage.DRAFT_AREA, "sentUsingSelectEmail",
                                              "Verify select configured mail from mail will be sent using dropdown")
            return False

    def select_configured_mail_dropdown(self):
        overlayPane = self.get_element(Locators.MailDraftPage.OVERLAY_PANE)
        EmailId = overlayPane.find_element(*Locators.MailDraftPage.MAIL_WILL_BE_SENT_USING_EMAIL_ID_DROP_DOWN)
        EmailId.click()
        time.sleep(1)
