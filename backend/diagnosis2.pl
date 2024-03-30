% Rules for faulty components
faulty_graphics_card(blank_screen).
faulty_graphics_card(artifacting_on_screen).
faulty_graphics_card(flickering_display).

faulty_audio_card(no_sound).

faulty_monitor(blank_screen).

loose_display_cable(blank_screen).
loose_display_cable(flickering_display).

faulty_speakers(no_sound).

mute_setting_enabled(no_sound).

overheating(computer_freezing).
overheating(random_shutdowns).
overheating(loud_fan_noise).
overheating(artifacting_on_screen).
overheating(computer_overheating).
overheating(spontaneous_rebooting).

insufficient_memory(computer_freezing).
insufficient_memory(slow_performance).
insufficient_memory(high_CPU_usage).

faulty_hard_drive(computer_freezing).
faulty_hard_drive(random_shutdowns).
faulty_hard_drive(computer_not_booting_to_OS).

too_many_background_processes(slow_performance).
too_many_background_processes(high_CPU_usage).

disk_fragmentation(slow_performance).

faulty_memory(blue_screen_of_death).

corrupted_system_files(blue_screen_of_death).
corrupted_system_files(random_shutdowns).
corrupted_system_files(usb_device_not_recognized).

driver_conflict(blue_screen_of_death).

faulty_network_adapter(network_connection_issues).

misconfigured_network_settings(network_connection_issues).

interference(network_connection_issues).

loose_keyboard_cable(unresponsive_keyboard).

driver_issues(unresponsive_keyboard).
driver_issues(artifacting_on_screen).
driver_issues(usb_device_not_recognized).
driver_issues(flickering_display).
driver_issues(spontaneous_rebooting).

faulty_keyboard(unresponsive_keyboard).

faulty_fan(loud_fan_noise).
faulty_fan(computer_overheating).

dusty_components(loud_fan_noise).
dusty_components(artifacting_on_screen).
dusty_components(loud_hard_drive_noise).
dusty_components(computer_overheating).

faulty_USB_port(usb_device_not_recognized).

faulty_power_supply(random_shutdowns).
faulty_power_supply(spontaneous_rebooting).

faulty_motherboard(computer_wont_power_on).

corrupted_boot_loader(computer_not_booting_to_OS).

missing_boot_files(computer_not_booting_to_OS).

printer_paper_jam(printer_not_printing).

printer_offline(printer_not_printing).

malware_infection(high_CPU_usage).

blocked_airflow(computer_overheating).

improper_drive_installation(loud_hard_drive_noise).

printer_driver_issues(printer_not_printing).

failing_hard_drive(loud_hard_drive_noise).

% Rules for diagnosis of compound issues
diagnose_compound_issue(computer_overheating, dusty_components).
diagnose_compound_issue(faulty_graphics_card, driver_issues).

% Rule for diagnosing multiple symptoms
diagnose_symptom([], []).
diagnose_symptom([Symptom|Rest], Diagnosis) :-
    diagnose_issue(Symptom, Issue),
    diagnose_symptom(Rest, RestDiagnosis),
    (memberchk(Issue, RestDiagnosis) -> Diagnosis = RestDiagnosis ; append([Issue], RestDiagnosis, Diagnosis)).

% Rules for diagnosing issues based on symptoms
diagnose_issue(Symptom, Issue) :-
    faulty_graphics_card(Symptom),
    Issue = faulty_graphics_card.

diagnose_issue(Symptom, Issue) :-
    faulty_audio_card(Symptom),
    Issue = faulty_audio_card.

% Define rules for other symptoms and corresponding issues as needed.
