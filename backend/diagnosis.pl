:- use_module(library(persistency)).

% Define a predicate to initialize the persistency for the dynamic predicates
:- persistent faulty_symptoms(fault:atom, symptom:atom).

% Initialize persistency for the predicates
:- initialization(db_attach('faulty_symptoms.db', [])).

% Define symptoms associated with each issue

faulty_graphics_card_symptoms([blank_screen, artifacting_on_screen, flickering_display]).
faulty_audio_card_symptoms([no_sound]).
faulty_monitor_symptoms([blank_screen]).
loose_display_cable_symptoms([blank_screen, flickering_display]).
faulty_speakers_symptoms([no_sound]).
mute_setting_enabled_symptoms([no_sound]).
overheating_symptoms([computer_freezing, random_shutdowns, loud_fan_noise, artifacting_on_screen, computer_overheating, spontaneous_rebooting]).
insufficient_memory_symptoms([computer_freezing, slow_performance, high_CPU_usage]).
faulty_hard_drive_symptoms([computer_freezing, random_shutdowns, computer_not_booting_to_OS]).
too_many_background_processes_symptoms([slow_performance, high_CPU_usage]).
disk_fragmentation_symptoms([slow_performance]).
faulty_memory_symptoms([blue_screen_of_death]).
corrupted_system_files_symptoms([blue_screen_of_death, random_shutdowns, usb_device_not_recognized]).
driver_conflict_symptoms([blue_screen_of_death]).
faulty_network_adapter_symptoms([network_connection_issues]).
misconfigured_network_settings_symptoms([network_connection_issues]).
interference_symptoms([network_connection_issues]).
loose_keyboard_cable_symptoms([unresponsive_keyboard]).
driver_issues_symptoms([unresponsive_keyboard, artifacting_on_screen, usb_device_not_recognized, flickering_display, spontaneous_rebooting]).
faulty_keyboard_symptoms([unresponsive_keyboard]).
faulty_fan_symptoms([loud_fan_noise, computer_overheating]).
dusty_components_symptoms([loud_fan_noise, artifacting_on_screen, loud_hard_drive_noise, computer_overheating]).
faulty_USB_port_symptoms([usb_device_not_recognized]).
faulty_power_supply_symptoms([random_shutdowns, spontaneous_rebooting]).
faulty_motherboard_symptoms([computer_wont_power_on]).
corrupted_boot_loader_symptoms([computer_not_booting_to_OS]).
missing_boot_files_symptoms([computer_not_booting_to_OS]).
printer_paper_jam_symptoms([printer_not_printing]).
printer_offline_symptoms([printer_not_printing]).
malware_infection_symptoms([high_CPU_usage]).
blocked_airflow_symptoms([computer_overheating]).
improper_drive_installation_symptoms([loud_hard_drive_noise]).
printer_driver_issues_symptoms([printer_not_printing]).
failing_hard_drive_symptoms([loud_hard_drive_noise]).

% Define dynamic predicates for symptoms


:- dynamic faulty_graphics_card_symptoms/1.
:- dynamic faulty_audio_card_symptoms/1.
:- dynamic faulty_monitor_symptoms/1.
:- dynamic loose_display_cable_symptoms/1.
:- dynamic faulty_speakers_symptoms/1.
:- dynamic mute_setting_enabled_symptoms/1.
:- dynamic overheating_symptoms/1.
:- dynamic insufficient_memory_symptoms/1.
:- dynamic faulty_hard_drive_symptoms/1.
:- dynamic too_many_background_processes_symptoms/1.
:- dynamic disk_fragmentation_symptoms/1.
:- dynamic faulty_memory_symptoms/1.
:- dynamic corrupted_system_files_symptoms/1.
:- dynamic driver_conflict_symptoms/1.
:- dynamic faulty_network_adapter_symptoms/1.
:- dynamic misconfigured_network_settings_symptoms/1.
:- dynamic interference_symptoms/1.
:- dynamic loose_keyboard_cable_symptoms/1.
:- dynamic driver_issues_symptoms/1.
:- dynamic faulty_keyboard_symptoms/1.
:- dynamic faulty_fan_symptoms/1.
:- dynamic dusty_components_symptoms/1.
:- dynamic faulty_USB_port_symptoms/1.
:- dynamic faulty_power_supply_symptoms/1.
:- dynamic faulty_motherboard_symptoms/1.
:- dynamic corrupted_boot_loader_symptoms/1.
:- dynamic missing_boot_files_symptoms/1.
:- dynamic printer_paper_jam_symptoms/1.
:- dynamic printer_offline_symptoms/1.
:- dynamic malware_infection_symptoms/1.
:- dynamic blocked_airflow_symptoms/1.
:- dynamic improper_drive_installation_symptoms/1.
:- dynamic printer_driver_issues_symptoms/1.
:- dynamic failing_hard_drive_symptoms/1.

% Rules for diagnosing issues based on symptoms

diagnose_issue(Symptoms, faulty_graphics_card) :-
    faulty_graphics_card_symptoms(Symptoms).

diagnose_issue(Symptoms, faulty_audio_card) :-
    faulty_audio_card_symptoms(Symptoms).

diagnose_issue(Symptoms, faulty_monitor) :-
    faulty_monitor_symptoms(Symptoms).

diagnose_issue(Symptoms, loose_display_cable) :-
    loose_display_cable_symptoms(Symptoms).

diagnose_issue(Symptoms, faulty_speakers) :-
    faulty_speakers_symptoms(Symptoms).

diagnose_issue(Symptoms, mute_setting_enabled) :-
    mute_setting_enabled_symptoms(Symptoms).

diagnose_issue(Symptoms, overheating) :-
    overheating_symptoms(Symptoms).

diagnose_issue(Symptoms, insufficient_memory) :-
    insufficient_memory_symptoms(Symptoms).

diagnose_issue(Symptoms, faulty_hard_drive) :-
    faulty_hard_drive_symptoms(Symptoms).

diagnose_issue(Symptoms, too_many_background_processes) :-
    too_many_background_processes_symptoms(Symptoms).

diagnose_issue(Symptoms, disk_fragmentation) :-
    disk_fragmentation_symptoms(Symptoms).

diagnose_issue(Symptoms, faulty_memory) :-
    faulty_memory_symptoms(Symptoms).

diagnose_issue(Symptoms, corrupted_system_files) :-
    corrupted_system_files_symptoms(Symptoms).

diagnose_issue(Symptoms, driver_conflict) :-
    driver_conflict_symptoms(Symptoms).

diagnose_issue(Symptoms, faulty_network_adapter) :-
    faulty_network_adapter_symptoms(Symptoms).

diagnose_issue(Symptoms, misconfigured_network_settings) :-
    misconfigured_network_settings_symptoms(Symptoms).

diagnose_issue(Symptoms, interference) :-
    interference_symptoms(Symptoms).

diagnose_issue(Symptoms, loose_keyboard_cable) :-
    loose_keyboard_cable_symptoms(Symptoms).

diagnose_issue(Symptoms, driver_issues) :-
    driver_issues_symptoms(Symptoms).

diagnose_issue(Symptoms, faulty_keyboard) :-
    faulty_keyboard_symptoms(Symptoms).

diagnose_issue(Symptoms, faulty_fan) :-
    faulty_fan_symptoms(Symptoms).

diagnose_issue(Symptoms, dusty_components) :-
    dusty_components_symptoms(Symptoms).

diagnose_issue(Symptoms, faulty_USB_port) :-
    faulty_USB_port_symptoms(Symptoms).

diagnose_issue(Symptoms, faulty_power_supply) :-
    faulty_power_supply_symptoms(Symptoms).

diagnose_issue(Symptoms, faulty_motherboard) :-
    faulty_motherboard_symptoms(Symptoms).

diagnose_issue(Symptoms, corrupted_boot_loader) :-
    corrupted_boot_loader_symptoms(Symptoms).

diagnose_issue(Symptoms, missing_boot_files) :-
    missing_boot_files_symptoms(Symptoms).

diagnose_issue(Symptoms, printer_paper_jam) :-
    printer_paper_jam_symptoms(Symptoms).

diagnose_issue(Symptoms, printer_offline) :-
    printer_offline_symptoms(Symptoms).

diagnose_issue(Symptoms, malware_infection) :-
    malware_infection_symptoms(Symptoms).

diagnose_issue(Symptoms, blocked_airflow) :-
    blocked_airflow_symptoms(Symptoms).

diagnose_issue(Symptoms, improper_drive_installation) :-
    improper_drive_installation_symptoms(Symptoms).

diagnose_issue(Symptoms, printer_driver_issues) :-
    printer_driver_issues_symptoms(Symptoms).

diagnose_issue(Symptoms, failing_hard_drive) :-
    failing_hard_drive_symptoms(Symptoms).

% Define the main predicate to diagnose issues based on a list of symptoms
diagnose_issues(Symptoms, Issues) :-
    findall(Issue, diagnose_issue(Symptoms, Issue), Issues).