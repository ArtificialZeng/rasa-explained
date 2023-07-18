.
├── binder
│   └── postBuild
├── changelog
│   ├── 12371.doc.md
│   ├── 12480.improvement.md
│   ├── 12514.improvement.md
│   ├── 12516.bugfix.md
│   ├── 12521.bugfix.md
│   ├── 12533.improvement.md
│   ├── 12543.improvement.md
│   ├── 12556.bugfix.md
│   ├── 12558.improvement.md
│   ├── 12637.improvement.md
│   ├── 12638.bugfix.md
│   ├── README.md
│   └── _template.md.jinja2
├── CHANGELOG.mdx
├── cloudbuild.yaml
├── CODE_OF_CONDUCT.md
├── CODEOWNERS
├── CONTRIBUTING.md
├── data
│   ├── configs_for_docs
│   │   ├── config_featurizers.yml
│   │   ├── default_config.yml
│   │   ├── default_english_config.yml
│   │   ├── default_spacy_config.yml
│   │   ├── example_for_suggested_config_after_train.yml
│   │   ├── example_for_suggested_config.yml
│   │   ├── pretrained_embeddings_convert_config.yml
│   │   ├── pretrained_embeddings_mitie_config_1.yml
│   │   ├── pretrained_embeddings_mitie_config_2.yml
│   │   ├── pretrained_embeddings_spacy_config.yml
│   │   └── supervised_embeddings_config.yml
│   ├── examples
│   │   ├── dialogflow
│   │   │   ├── agent.json
│   │   │   ├── entities
│   │   │   │   ├── cuisine_entries_en.json
│   │   │   │   ├── cuisine_entries_es.json
│   │   │   │   ├── cuisine.json
│   │   │   │   ├── flightNumber_entries_en.json
│   │   │   │   ├── flightNumber.json
│   │   │   │   ├── location_entries_en.json
│   │   │   │   ├── location_entries_es.json
│   │   │   │   └── location.json
│   │   │   ├── intents
│   │   │   │   ├── affirm.json
│   │   │   │   ├── affirm_usersays_en.json
│   │   │   │   ├── affirm_usersays_es.json
│   │   │   │   ├── Default Fallback Intent.json
│   │   │   │   ├── goodbye.json
│   │   │   │   ├── goodbye_usersays_en.json
│   │   │   │   ├── goodbye_usersays_es.json
│   │   │   │   ├── hi.json
│   │   │   │   ├── hi_usersays_en.json
│   │   │   │   ├── hi_usersays_es.json
│   │   │   │   ├── inform.json
│   │   │   │   ├── inform_usersays_en.json
│   │   │   │   └── inform_usersays_es.json
│   │   │   └── package.json
│   │   ├── luis
│   │   │   └── demo-restaurants_v7.json
│   │   ├── rasa
│   │   │   ├── demo-rasa.json
│   │   │   ├── demo-rasa-multi-intent.yml
│   │   │   ├── demo-rasa-responses.yml
│   │   │   └── demo-rasa.yml
│   │   └── wit
│   │       └── demo-flights.json
│   ├── graph_schemas
│   │   ├── config_pretrained_embeddings_mitie_predict_schema.yml
│   │   ├── config_pretrained_embeddings_mitie_train_schema.yml
│   │   ├── config_pretrained_embeddings_mitie_zh_predict_schema.yml
│   │   ├── config_pretrained_embeddings_mitie_zh_train_schema.yml
│   │   ├── config_pretrained_embeddings_spacy_duckling_predict_schema.yml
│   │   ├── config_pretrained_embeddings_spacy_duckling_train_schema.yml
│   │   ├── default_config_core_predict_schema.yml
│   │   ├── default_config_core_train_schema.yml
│   │   ├── default_config_e2e_predict_schema.yml
│   │   ├── default_config_e2e_train_schema.yml
│   │   ├── default_config_finetune_epoch_fraction_schema.yml
│   │   ├── default_config_finetune_schema.yml
│   │   ├── default_config_nlu_predict_schema.yml
│   │   ├── default_config_nlu_train_schema.yml
│   │   ├── default_config_predict_schema.yml
│   │   ├── default_config_train_schema.yml
│   │   ├── graph_config_short_predict_schema.yml
│   │   ├── graph_config_short_train_schema.yml
│   │   ├── keyword_classifier_config_predict_schema.yml
│   │   ├── keyword_classifier_config_train_schema.yml
│   │   ├── max_hist_config_predict_schema.yml
│   │   └── max_hist_config_train_schema.yml
│   ├── rasa_yaml_examples
│   │   └── nlu.yml
│   ├── README.md
│   ├── test
│   │   ├── config_embedding_test.yml
│   │   ├── demo-rasa-composite-entities.yml
│   │   ├── demo-rasa-lookup-ents.yml
│   │   ├── demo-rasa-more-ents-and-multiplied.yml
│   │   ├── demo-rasa-noents.json
│   │   ├── demo-rasa-no-ents.yml
│   │   ├── demo-rasa-small.json
│   │   ├── demo-rasa-zh.json
│   │   ├── dialogflow_en_converted_to_rasa.json
│   │   ├── dialogflow_es_converted_to_rasa.json
│   │   ├── duplicate_intents_yaml
│   │   │   ├── demo-rasa-intents-1.yml
│   │   │   ├── demo-rasa-intents-2.yml
│   │   │   └── demo-rasa-intents-3.yml
│   │   ├── hf_transformers_models.txt
│   │   ├── incorrect_nlu_format.yml
│   │   ├── lookup_tables
│   │   │   ├── lookup_table.json
│   │   │   ├── lookup_table.yml
│   │   │   └── plates.txt
│   │   ├── luis_converted_to_rasa.json
│   │   ├── many_intents.yml
│   │   ├── md_converted_to_json.json
│   │   ├── multiple_files_json
│   │   │   ├── demo-rasa-affirm.json
│   │   │   ├── demo-rasa-chitchat.json
│   │   │   ├── demo-rasa-goodbye.json
│   │   │   ├── demo-rasa-greet.json
│   │   │   └── demo-rasa-restaurant_search.json
│   │   ├── overlapping_regex_entities.yml
│   │   ├── simple_retrieval_intent_nlu.yml
│   │   ├── stories_default_retrieval_intents.yml
│   │   ├── synonyms_only.yml
│   │   ├── test_integration
│   │   │   ├── data
│   │   │   │   ├── nlu.yml
│   │   │   │   ├── rules.yml
│   │   │   │   └── stories.yml
│   │   │   └── domain.yml
│   │   ├── test_integration_err
│   │   │   ├── data
│   │   │   │   ├── nlu.yml
│   │   │   │   ├── rules.yml
│   │   │   │   └── stories.yml
│   │   │   └── domain.yml
│   │   ├── training_data_containing_special_chars.json
│   │   └── wit_converted_to_rasa.json
│   ├── test_action_extract_slots_11333
│   │   ├── config.yml
│   │   ├── data
│   │   │   ├── nlu.yml
│   │   │   └── stories.yml
│   │   ├── domain.yml
│   │   ├── models
│   │   └── tests
│   │       └── test_stories.yml
│   ├── test_classes
│   │   ├── custom_graph_components
│   │   │   ├── nlu_dense.py
│   │   │   ├── nlu_meta_fallback.py
│   │   │   ├── nlu_meta_intent_featurizer.py
│   │   │   └── nlu_sparse.py
│   │   ├── custom_slots.py
│   │   ├── graph_component_interface.py
│   │   ├── nlu_component_skeleton.py
│   │   └── registered_component.py
│   ├── test_config
│   │   ├── config_crf_custom_features.yml
│   │   ├── config_crf_no_pattern_feature.yml
│   │   ├── config_crf_no_regex.yml
│   │   ├── config_crf_no_synonyms.yml
│   │   ├── config_default_assistant_id_value.yml
│   │   ├── config_defaults.yml
│   │   ├── config_embedding_intent_response_selector.yml
│   │   ├── config_empty_en_after_dumping_core.yml
│   │   ├── config_empty_en_after_dumping_nlu.yml
│   │   ├── config_empty_en_after_dumping.yml
│   │   ├── config_empty_en.yml
│   │   ├── config_empty_fr_after_dumping.yml
│   │   ├── config_empty_fr.yml
│   │   ├── config_language_only.yml
│   │   ├── config_no_assistant_id_with_comments.yml
│   │   ├── config_no_assistant_id.yml
│   │   ├── config_pipeline_empty.yml
│   │   ├── config_pipeline_missing.yml
│   │   ├── config_policies_empty.yml
│   │   ├── config_policies_missing.yml
│   │   ├── config_pretrained_embeddings_convert.yml
│   │   ├── config_pretrained_embeddings_mitie_2.yml
│   │   ├── config_pretrained_embeddings_mitie_diet.yml
│   │   ├── config_pretrained_embeddings_mitie.yml
│   │   ├── config_pretrained_embeddings_mitie_zh.yml
│   │   ├── config_pretrained_embeddings_spacy_de.yml
│   │   ├── config_pretrained_embeddings_spacy_duckling.yml
│   │   ├── config_pretrained_embeddings_spacy.yml
│   │   ├── config_response_selector_minimal.yml
│   │   ├── config_spacy_entity_extractor.yml
│   │   ├── config_supervised_embeddings_duckling.yml
│   │   ├── config_supervised_embeddings.yml
│   │   ├── config_ted_policy_model_checkpointing.yml
│   │   ├── config_ted_policy_model_checkpointing_zero_eval_num_examples.yml
│   │   ├── config_ted_policy_model_checkpointing_zero_every_num_epochs.yml
│   │   ├── config_ted_policy_no_model_checkpointing.yml
│   │   ├── config_train_server_json.yml
│   │   ├── config_train_server_md.yml
│   │   ├── config_unique_assistant_id.yml
│   │   ├── config_with_comment_between_suggestions.yml
│   │   ├── config_with_comments_after_dumping.yml
│   │   ├── config_with_comments.yml
│   │   ├── embedding_random_seed.yaml
│   │   ├── example_config.yaml
│   │   ├── graph_config_short.yml
│   │   ├── graph_config.yml
│   │   ├── keyword_classifier_config.yml
│   │   ├── max_hist_config.yml
│   │   ├── no_max_hist_config.yml
│   │   ├── stack_config.yml
│   │   └── test_moodbot_config_no_assistant_id.yml
│   ├── test_custom_action_triggers_action_extract_slots
│   │   ├── config.yml
│   │   ├── domain.yml
│   │   ├── nlu.yml
│   │   └── stories.yml
│   ├── test_domains
│   │   ├── conditional_response_variations.yml
│   │   ├── custom_slot_domain.yml
│   │   ├── default_retrieval_intents.yml
│   │   ├── default_unfeaturized_entities.yml
│   │   ├── default_with_mapping.yml
│   │   ├── default_with_slots.yml
│   │   ├── default.yml
│   │   ├── domain_with_categorical_slot.yml
│   │   ├── duplicate_actions.yml
│   │   ├── duplicate_entities.yml
│   │   ├── duplicate_intents.yml
│   │   ├── duplicate_responses.yml
│   │   ├── empty_response_format.yml
│   │   ├── form.yml
│   │   ├── initial_slot_values_greet_and_goodbye.yml
│   │   ├── invalid_format.yml
│   │   ├── minimal_domain_validate_files_with_active_loop_null.yml
│   │   ├── missing_chitchat_response.yml
│   │   ├── missing_text_for_templates.yml
│   │   ├── mixed_retrieval_intents.yml
│   │   ├── people_form.yml
│   │   ├── query_form.yml
│   │   ├── response_selector_responses_in_domain.yml
│   │   ├── restaurant_form.yml
│   │   ├── selectors.yml
│   │   ├── simple_retrieval_intent.yml
│   │   ├── test_domain_files_with_no_session_config_and_custom_session_config
│   │   │   ├── config.yml
│   │   │   ├── data
│   │   │   │   ├── nlu.yml
│   │   │   │   ├── responses.yml
│   │   │   │   └── stories.yml
│   │   │   └── domain.yml
│   │   ├── test_domain_from_directory
│   │   │   ├── domain_invalid.yml
│   │   │   └── domain_valid.yml
│   │   ├── test_domain_from_directory_for_entities
│   │   │   ├── game_1.yml
│   │   │   ├── game_2.yml
│   │   │   └── game_3.yml
│   │   ├── test_domain_from_directory_tree
│   │   │   ├── domain_pt1.yml
│   │   │   ├── skill_1_domain
│   │   │   │   └── domain_pt2.yml
│   │   │   └── skill_2_domain
│   │   │       ├── domain_pt3.yml
│   │   │       └── skill_2_subdirectory
│   │   ├── test_domain_from_multiple_files
│   │   │   ├── drum.yml
│   │   │   ├── last_month.yml
│   │   │   ├── main_menu.yml
│   │   │   ├── selection.yml
│   │   │   ├── small_talk.yml
│   │   │   ├── tomorrow.yml
│   │   │   └── wallets.yml
│   │   ├── test_domain_with_duplicates
│   │   │   ├── domain1.yml
│   │   │   └── domain2.yml
│   │   ├── test_domain_without_duplicates
│   │   │   ├── domain1.yml
│   │   │   └── domain2.yml
│   │   ├── test_domain_with_separate_session_config
│   │   │   ├── configuration.yml
│   │   │   ├── intents.yml
│   │   │   └── responses.yml
│   │   ├── travel_form.yml
│   │   ├── valid_actions.yml
│   │   ├── wrong_custom_response_format.yml
│   │   └── wrong_response_format.yml
│   ├── test_e2ebot
│   │   ├── config.yml
│   │   ├── data
│   │   │   ├── nlu.yml
│   │   │   └── stories.yml
│   │   ├── domain.yml
│   │   └── tests
│   │       ├── test_stories_with_unknown_bot_utterances.yml
│   │       └── test_stories.yml
│   ├── test_endpoints
│   │   ├── cert.pem
│   │   ├── custom_tracker_endpoints.yml
│   │   ├── endpoints_redis.yml
│   │   ├── endpoints_sql.yml
│   │   ├── event_brokers
│   │   │   ├── kafka_invalid_sasl_mechanism.yml
│   │   │   ├── kafka_invalid_security_protocol.yml
│   │   │   ├── kafka_plaintext_endpoint_no_url.yml
│   │   │   ├── kafka_plaintext_endpoint.yml
│   │   │   ├── kafka_sasl_plaintext_endpoint.yml
│   │   │   ├── kafka_sasl_ssl_endpoint.yml
│   │   │   ├── kafka_ssl_endpoint.yml
│   │   │   ├── pika_endpoint.yml
│   │   │   └── sql_endpoint.yml
│   │   ├── example_endpoints.yml
│   │   ├── __init__.py
│   │   └── model_endpoint.yml
│   ├── test_evaluations
│   │   ├── test_end_to_end_story.yml
│   │   ├── test_end_to_end_trips_circuit_breaker.yml
│   │   ├── test_form_end_to_end_stories.yml
│   │   ├── test_stories_trip_circuit_breaker.yml
│   │   └── test_story_unknown_entity.yml
│   ├── test_from_trigger_intent_with_mapping_conditions
│   │   ├── config.yml
│   │   ├── domain.yml
│   │   ├── nlu.yml
│   │   └── stories.yml
│   ├── test_from_trigger_intent_with_no_mapping_conditions
│   │   ├── config.yml
│   │   ├── domain.yml
│   │   ├── nlu.yml
│   │   └── stories.yml
│   ├── test_incremental_training
│   │   ├── iter1
│   │   │   ├── nlg_training_data.yml
│   │   │   └── training_data.yml
│   │   └── iter2
│   │       └── training_data.yml
│   ├── test_logging_config_files
│   │   ├── test_invalid_format_value_in_config.yml
│   │   ├── test_invalid_handler_key_in_config.yml
│   │   ├── test_invalid_value_for_level_in_config.yml
│   │   ├── test_logging_config.yml
│   │   ├── test_missing_required_key_invalid_config.yml
│   │   └── test_non_existent_handler_id.yml
│   ├── test_mixed_yaml_training_data
│   │   └── training_data.yml
│   ├── test_moodbot
│   │   ├── config.yml
│   │   ├── credentials.yml
│   │   ├── data
│   │   │   ├── nlu.yml
│   │   │   ├── rules.yml
│   │   │   └── stories.yml
│   │   ├── domain.yml
│   │   └── unexpected_intent_policy_config.yml
│   ├── test_multi_domain
│   │   ├── config.yml
│   │   ├── data
│   │   │   ├── GreetBot
│   │   │   │   ├── data
│   │   │   │   └── domain.yml
│   │   │   ├── MoodBot
│   │   │   │   ├── config.yml
│   │   │   │   ├── data
│   │   │   │   └── domain.yml
│   │   │   ├── nlu.yml
│   │   │   └── stories.yml
│   │   └── domain.yml
│   ├── test_multifile_yaml_stories
│   │   ├── stories_part_1.yml
│   │   └── stories_part_2.yml
│   ├── test_multiline_intent_examples_yaml
│   │   └── nlu.yml
│   ├── test_multiproject
│   │   ├── config.yml
│   │   └── projects
│   │       ├── ChitchatBot
│   │       │   ├── data
│   │       │   └── domain.yml
│   │       └── GreetBot
│   │           ├── data
│   │           └── domain.yml
│   ├── test_nlu
│   │   └── test_nlu_validate_files_with_active_loop_null.yml
│   ├── test_nlu_no_responses
│   │   ├── domain_with_only_responses.yml
│   │   ├── nlu_no_responses.yml
│   │   ├── nlu_with_unicode.yml
│   │   └── sara_nlu_data.yml
│   ├── test_number_nlu_examples
│   │   ├── nlu.yml
│   │   ├── rules.yml
│   │   └── stories.yml
│   ├── test_responses
│   │   ├── default.yml
│   │   └── responses_utter_rasa.yml
│   ├── test_response_selector_bot
│   │   ├── config.yml
│   │   ├── data
│   │   │   ├── nlu.yml
│   │   │   └── rules.yml
│   │   ├── domain.yml
│   │   ├── __init__.py
│   │   └── tests
│   │       └── test_stories.yml
│   ├── test_restaurantbot
│   │   ├── config.yml
│   │   ├── data
│   │   │   ├── nlu.yml
│   │   │   ├── rules.yml
│   │   │   └── stories.yml
│   │   └── domain.yml
│   ├── test_selectors
│   │   └── nlu.yml
│   ├── test_spacybot
│   │   ├── config.yml
│   │   ├── data
│   │   │   ├── nlu.yml
│   │   │   └── stories.yml
│   │   └── domain.yml
│   ├── test_tokenizers
│   │   └── naughty_strings.json
│   ├── test_trackers
│   │   ├── tracker_moodbot.json
│   │   └── tracker_moodbot_with_new_utterances.json
│   ├── test_validation
│   │   ├── data
│   │   │   ├── nlu.yml
│   │   │   └── stories.yml
│   │   └── domain.yml
│   ├── test_wrong_yaml_stories
│   │   ├── intent_with_leading_slash.yml
│   │   └── wrong_yaml.yml
│   └── test_yaml_stories
│       ├── non_test_full_retrieval_intent_story.yml
│       ├── rules_greet_and_goodbye.yml
│       ├── rules_missing_intent.yml
│       ├── rules_without_stories_and_wrong_names.yml
│       ├── rules_without_stories.yml
│       ├── rules_with_stories_sorted.yaml
│       ├── simple_story_with_only_end.yml
│       ├── stories_and_rules.yml
│       ├── stories_checkpoint_after_or.yml
│       ├── stories_conflicting_1.yml
│       ├── stories_conflicting_2.yml
│       ├── stories_conflicting_3.yml
│       ├── stories_conflicting_4.yml
│       ├── stories_conflicting_5.yml
│       ├── stories_conflicting_6.yml
│       ├── stories_conflicting_at_1.yml
│       ├── stories_defaultdomain.yml
│       ├── stories_e2e.yml
│       ├── stories_form.yml
│       ├── stories_hybrid_e2e.yml
│       ├── stories_missing_intent.yml
│       ├── stories_restart.yml
│       ├── stories_retrieval_intents.yml
│       ├── stories_simple.yml
│       ├── stories_unexpected_intent_unlearnable.yml
│       ├── stories_unfeaturized_entities.yml
│       ├── stories_unused_checkpoints.yml
│       ├── stories_with_cycle.yml
│       ├── stories_with_rules_conflicting.yml
│       ├── stories.yml
│       ├── story_slot_different_types.yml
│       ├── story_with_or_and_entities_with_no_value.yml
│       ├── story_with_or_and_entities.yml
│       ├── story_with_or_slot_was_set.yml
│       ├── story_with_slot_was_set.yml
│       ├── story_with_two_equal_or_statements.yml
│       ├── test_base_retrieval_intent_story.yml
│       ├── test_base_retrieval_intent_wrong_prediction.yml
│       ├── test_failed_entity_extraction_comment.yml
│       ├── test_full_retrieval_intent_story.yml
│       ├── test_full_retrieval_intent_wrong_prediction.yml
│       ├── test_multiple_action_unlikely_intent_warnings.yml
│       ├── test_prediction_with_correct_intent_wrong_entity.yml
│       ├── test_prediction_with_wrong_intent_correct_entity.yml
│       ├── test_prediction_with_wrong_intent_wrong_entity.yml
│       └── test_stories_entity_annotations.yml
├── docker
│   ├── configs
│   │   ├── config_pretrained_embeddings_mitie.yml
│   │   ├── config_pretrained_embeddings_spacy_de.yml
│   │   ├── config_pretrained_embeddings_spacy_en_duckling.yml
│   │   ├── config_pretrained_embeddings_spacy_en.yml
│   │   └── config_pretrained_embeddings_spacy_it.yml
│   ├── docker-bake.hcl
│   ├── docker-cloud.yml
│   ├── docker-compose.yml
│   ├── Dockerfile.base
│   ├── Dockerfile.base-builder
│   ├── Dockerfile.base-mitie
│   ├── Dockerfile.base-poetry
│   ├── Dockerfile.full
│   ├── Dockerfile.pretrained_embeddings_mitie_en
│   ├── Dockerfile.pretrained_embeddings_spacy_de
│   ├── Dockerfile.pretrained_embeddings_spacy_en
│   └── Dockerfile.pretrained_embeddings_spacy_it
├── Dockerfile
├── docs
│   ├── babel.config.js
│   ├── docs
│   │   ├── action-server
│   │   │   ├── actions.mdx
│   │   │   ├── events.mdx
│   │   │   ├── index.mdx
│   │   │   ├── knowledge-base-actions.mdx
│   │   │   ├── running-action-server.mdx
│   │   │   ├── sdk-actions.mdx
│   │   │   ├── sdk-dispatcher.mdx
│   │   │   ├── sdk-events.mdx
│   │   │   ├── sdk-tracker.mdx
│   │   │   └── validation-action.mdx
│   │   ├── actions.mdx
│   │   ├── architecture-img.png
│   │   ├── architecture.mdx
│   │   ├── arch-overview.mdx
│   │   ├── business-logic.mdx
│   │   ├── chitchat-faqs.mdx
│   │   ├── command-line-interface.mdx
│   │   ├── compatibility-matrix.mdx
│   │   ├── component-lifecycle-img.png
│   │   ├── components.mdx
│   │   ├── connectors
│   │   │   ├── audioodes-voiceai-connect.mdx
│   │   │   ├── cisco-webex-teams.mdx
│   │   │   ├── custom-connectors.mdx
│   │   │   ├── facebook-messenger.mdx
│   │   │   ├── hangouts.mdx
│   │   │   ├── img
│   │   │   │   ├── slack-app-home.png
│   │   │   │   ├── slack-create-app.png
│   │   │   │   ├── slack-events.png
│   │   │   │   ├── slack-install-app.png
│   │   │   │   ├── slack-interactivity.png
│   │   │   │   ├── slack-request-url.png
│   │   │   │   ├── slack-scopes.png
│   │   │   │   ├── slack-secret.png
│   │   │   │   ├── twilio-set-sip-webhook.png
│   │   │   │   └── twilio-set-webhook.png
│   │   │   ├── mattermost.mdx
│   │   │   ├── microsoft-bot-framework.mdx
│   │   │   ├── rocketchat.mdx
│   │   │   ├── slack.mdx
│   │   │   ├── telegram.mdx
│   │   │   ├── twilio.mdx
│   │   │   ├── twilio-voice.mdx
│   │   │   └── your-own-website.mdx
│   │   ├── contextual-conversations.mdx
│   │   ├── conversation-driven-development.mdx
│   │   ├── custom-actions.mdx
│   │   ├── custom-graph-components.mdx
│   │   ├── default-actions.mdx
│   │   ├── deploy
│   │   │   ├── deploy-action-server.mdx
│   │   │   ├── deploy-rasa.mdx
│   │   │   ├── deploy-rasa-pro-services.mdx
│   │   │   └── introduction.mdx
│   │   ├── docker
│   │   │   ├── building-in-docker.mdx
│   │   │   └── deploying-in-docker-compose.mdx
│   │   ├── domain.mdx
│   │   ├── event-brokers.mdx
│   │   ├── fallback-handoff.mdx
│   │   ├── forms.mdx
│   │   ├── generating-nlu-data.mdx
│   │   ├── glossary.mdx
│   │   ├── graph-recipe.mdx
│   │   ├── http-api.mdx
│   │   ├── installation
│   │   │   ├── environment-set-up.mdx
│   │   │   ├── installing-rasa-open-source.mdx
│   │   │   └── rasa-pro
│   │   │       ├── installation.mdx
│   │   │       └── rasa-pro-artifacts.mdx
│   │   ├── introduction.mdx
│   │   ├── jupyter-notebooks.mdx
│   │   ├── language-support.mdx
│   │   ├── llms
│   │   │   ├── intentless-meaning-compounds.png
│   │   │   ├── intentless-policy-interaction.png
│   │   │   ├── large-language-models.mdx
│   │   │   ├── llm-custom.mdx
│   │   │   ├── llm-IntentClassifier-docs.jpg
│   │   │   ├── llm-intentless.mdx
│   │   │   ├── llm-intent.mdx
│   │   │   ├── llm-nlg.mdx
│   │   │   └── llm-setup.mdx
│   │   ├── lock-stores.mdx
│   │   ├── markers.mdx
│   │   ├── messaging-and-voice-channels.mdx
│   │   ├── migrate-from
│   │   │   ├── dialogflow_export_2.png
│   │   │   ├── dialogflow_export.png
│   │   │   ├── facebook-wit-ai-to-rasa.mdx
│   │   │   ├── google-dialogflow-to-rasa.mdx
│   │   │   ├── ibm-watson-to-rasa.mdx
│   │   │   ├── luis_export.png
│   │   │   └── microsoft-luis-to-rasa.mdx
│   │   ├── migrate-from.mdx
│   │   ├── migration-guide.mdx
│   │   ├── model-configuration.mdx
│   │   ├── model-storage.mdx
│   │   ├── monitoring
│   │   │   ├── analytics
│   │   │   │   ├── data-structure-reference.mdx
│   │   │   │   ├── example-queries.mdx
│   │   │   │   ├── getting-started-with-analytics.mdx
│   │   │   │   └── realtime-markers.mdx
│   │   │   ├── load-testing-guidelines.mdx
│   │   │   └── tracing.mdx
│   │   ├── nlg.mdx
│   │   ├── nlu-only.mdx
│   │   ├── nlu-only-server.mdx
│   │   ├── nlu-training-data.mdx
│   │   ├── pii-management.mdx
│   │   ├── playground.mdx
│   │   ├── policies.mdx
│   │   ├── rasa-pro-changelog.mdx
│   │   ├── rasa-pro.mdx
│   │   ├── reaching-out-to-user.mdx
│   │   ├── responses.mdx
│   │   ├── rules.mdx
│   │   ├── sdk_changelog.mdx
│   │   ├── secrets-managers.mdx
│   │   ├── setting-up-ci-cd.mdx
│   │   ├── slot-validation-actions.mdx
│   │   ├── sources
│   │   ├── spaces.mdx
│   │   ├── stories.mdx
│   │   ├── telemetry
│   │   │   ├── events.json
│   │   │   └── telemetry.mdx
│   │   ├── testing-your-assistant.mdx
│   │   ├── tracker-stores.mdx
│   │   ├── training-data-format.mdx
│   │   ├── training-data-importers.mdx
│   │   ├── tuning-your-model.mdx
│   │   ├── unexpected-input.mdx
│   │   └── writing-stories.mdx
│   ├── docusaurus.config.js
│   ├── netlify.toml
│   ├── package.json
│   ├── plugins
│   │   ├── google-tagmanager
│   │   │   ├── client.js
│   │   │   └── index.js
│   │   ├── included_source.js
│   │   └── program_output.js
│   ├── pydoc-markdown.yml
│   ├── README.md
│   ├── scripts
│   │   ├── compile_included_sources.js
│   │   ├── compile_program_outputs.js
│   │   ├── compile_telemetry_reference.js
│   │   ├── compile_variables.js
│   │   ├── copy_md_files.js
│   │   └── update_versioned_sources.js
│   ├── sidebars.js
│   ├── static
│   │   ├── img
│   │   │   ├── analytics
│   │   │   │   ├── analytics-db-schema-old.png
│   │   │   │   ├── analytics-er-db.png
│   │   │   │   ├── analytics-er-rasa-action.png
│   │   │   │   ├── analytics-er-rasa-bot-message.png
│   │   │   │   ├── analytics-er-rasa-event.png
│   │   │   │   ├── analytics-er-rasa-sender.png
│   │   │   │   ├── analytics-er-rasa-session.png
│   │   │   │   ├── analytics-er-rasa-session-slot-state.png
│   │   │   │   ├── analytics-er-rasa-slot.png
│   │   │   │   ├── analytics-er-rasa-turn.png
│   │   │   │   ├── analytics-er-rasa-user-message.png
│   │   │   │   ├── analytics-examples.png
│   │   │   │   ├── graph-abandonment-rate.png
│   │   │   │   ├── graph-escalation-rate.png
│   │   │   │   ├── graph-intent-distribution.png
│   │   │   │   ├── graph-number-sessions-channel.png
│   │   │   │   ├── graph-number-sessions-month.png
│   │   │   │   ├── graph-top-5-intents.png
│   │   │   │   └── realtime-markers.png
│   │   │   ├── architecture.png
│   │   │   ├── blocks.png
│   │   │   ├── graph_architecture.png
│   │   │   ├── intent_confusion_matrix_example.png
│   │   │   ├── intent_histogram_example.png
│   │   │   ├── introduction.png
│   │   │   ├── logo-rasa-oss.png
│   │   │   ├── logo-rasa-x.png
│   │   │   ├── og-image.png
│   │   │   ├── rasa-plus-architecture.png
│   │   │   ├── rasa-pro-analytics-overview.png
│   │   │   ├── spaces_hierarchy.png
│   │   │   └── train-test-github-action.png
│   │   ├── js
│   │   │   └── rasa-chatblock.min.js
│   │   └── spec
│   │       ├── action-server.yml
│   │       └── rasa.yml
│   ├── themes
│   │   └── theme-custom
│   │       ├── custom.css
│   │       ├── index.js
│   │       └── theme
│   │           ├── AssistantBuilder
│   │           ├── CodeBlock
│   │           ├── Grid
│   │           ├── Playground
│   │           ├── Prototyper
│   │           ├── RasaButton
│   │           ├── RasaLabsBanner
│   │           ├── RasaLabsLabel
│   │           ├── RasaProBanner
│   │           ├── RasaProLabel
│   │           └── ReactLiveScope
│   └── yarn.lock
├── examples
│   ├── concertbot
│   │   ├── actions
│   │   │   ├── actions.py
│   │   │   └── __init__.py
│   │   ├── config.yml
│   │   ├── data
│   │   │   ├── nlu.yml
│   │   │   ├── rules.yml
│   │   │   └── stories.yml
│   │   ├── domain.yml
│   │   ├── endpoints.yml
│   │   └── README.md
│   ├── e2ebot
│   │   ├── config.yml
│   │   ├── data
│   │   │   ├── nlu.yml
│   │   │   └── stories.yml
│   │   ├── domain.yml
│   │   └── tests
│   │       └── test_stories.yml
│   ├── formbot
│   │   ├── actions
│   │   │   ├── actions.py
│   │   │   └── __init__.py
│   │   ├── config.yml
│   │   ├── data
│   │   │   ├── nlu.yml
│   │   │   ├── rules.yml
│   │   │   └── stories.yml
│   │   ├── domain.yml
│   │   ├── endpoints.yml
│   │   ├── README.md
│   │   └── tests
│   │       └── test_stories.yml
│   ├── __init__.py
│   ├── knowledgebasebot
│   │   ├── actions
│   │   │   ├── actions.py
│   │   │   └── __init__.py
│   │   ├── config.yml
│   │   ├── data
│   │   │   ├── nlu.yml
│   │   │   ├── rules.yml
│   │   │   └── stories.yml
│   │   ├── domain.yml
│   │   ├── endpoints.yml
│   │   ├── knowledge_base_data.json
│   │   └── README.md
│   ├── moodbot
│   │   ├── config.yml
│   │   ├── credentials.yml
│   │   ├── data
│   │   │   ├── nlu.yml
│   │   │   ├── rules.yml
│   │   │   └── stories.yml
│   │   ├── domain.yml
│   │   └── README.md
│   ├── nlg_server
│   │   ├── __init__.py
│   │   └── nlg_server.py
│   ├── reminderbot
│   │   ├── actions
│   │   │   ├── actions.py
│   │   │   └── __init__.py
│   │   ├── callback_server.py
│   │   ├── config.yml
│   │   ├── credentials.yml
│   │   ├── data
│   │   │   ├── nlu.yml
│   │   │   ├── rules.yml
│   │   │   └── stories.yml
│   │   ├── domain.yml
│   │   ├── endpoints.yml
│   │   └── README.md
│   ├── responseselectorbot
│   │   ├── config.yml
│   │   ├── data
│   │   │   ├── nlu.yml
│   │   │   ├── rules.yml
│   │   │   └── stories.yml
│   │   ├── domain.yml
│   │   └── README.md
│   └── rules
│       ├── actions
│       │   ├── actions.py
│       │   └── __init__.py
│       ├── config.yml
│       ├── data
│       │   ├── nlu.yml
│       │   └── rules.yml
│       ├── domain.yml
│       └── endpoints.yml
├── LICENSE.txt
├── Makefile
├── NOTICE
├── poetry.lock
├── PRINCIPLES.md
├── pyproject.toml
├── rasa
│   ├── api.py
│   ├── cli
│   │   ├── arguments
│   │   │   ├── data.py
│   │   │   ├── default_arguments.py
│   │   │   ├── evaluate.py
│   │   │   ├── export.py
│   │   │   ├── __init__.py
│   │   │   ├── interactive.py
│   │   │   ├── run.py
│   │   │   ├── shell.py
│   │   │   ├── test.py
│   │   │   ├── train.py
│   │   │   ├── visualize.py
│   │   │   └── x.py
│   │   ├── data.py
│   │   ├── evaluate.py
│   │   ├── export.py
│   │   ├── initial_project
│   │   │   ├── actions
│   │   │   │   ├── actions.py
│   │   │   │   └── __init__.py
│   │   │   ├── config.yml
│   │   │   ├── credentials.yml
│   │   │   ├── data
│   │   │   │   ├── nlu.yml
│   │   │   │   ├── rules.yml
│   │   │   │   └── stories.yml
│   │   │   ├── domain.yml
│   │   │   ├── endpoints.yml
│   │   │   └── tests
│   │   │       └── test_stories.yml
│   │   ├── __init__.py
│   │   ├── interactive.py
│   │   ├── run.py
│   │   ├── scaffold.py
│   │   ├── shell.py
│   │   ├── telemetry.py
│   │   ├── test.py
│   │   ├── train.py
│   │   ├── utils.py
│   │   ├── visualize.py
│   │   └── x.py
│   ├── constants.py
│   ├── core
│   │   ├── actions
│   │   │   ├── action.py
│   │   │   ├── constants.py
│   │   │   ├── forms.py
│   │   │   ├── __init__.py
│   │   │   ├── loops.py
│   │   │   └── two_stage_fallback.py
│   │   ├── agent.py
│   │   ├── brokers
│   │   │   ├── broker.py
│   │   │   ├── file.py
│   │   │   ├── __init__.py
│   │   │   ├── kafka.py
│   │   │   ├── pika.py
│   │   │   └── sql.py
│   │   ├── channels
│   │   │   ├── botframework.py
│   │   │   ├── callback.py
│   │   │   ├── channel.py
│   │   │   ├── console.py
│   │   │   ├── facebook.py
│   │   │   ├── hangouts.py
│   │   │   ├── __init__.py
│   │   │   ├── mattermost.py
│   │   │   ├── rasa_chat.py
│   │   │   ├── rest.py
│   │   │   ├── rocketchat.py
│   │   │   ├── slack.py
│   │   │   ├── socketio.py
│   │   │   ├── telegram.py
│   │   │   ├── twilio.py
│   │   │   ├── twilio_voice.py
│   │   │   └── webexteams.py
│   │   ├── constants.py
│   │   ├── evaluation
│   │   │   ├── __init__.py
│   │   │   ├── marker_base.py
│   │   │   ├── marker.py
│   │   │   ├── marker_stats.py
│   │   │   └── marker_tracker_loader.py
│   │   ├── exceptions.py
│   │   ├── exporter.py
│   │   ├── featurizers
│   │   │   ├── __init__.py
│   │   │   ├── precomputation.py
│   │   │   ├── single_state_featurizer.py
│   │   │   └── tracker_featurizers.py
│   │   ├── http_interpreter.py
│   │   ├── __init__.py
│   │   ├── jobs.py
│   │   ├── lock.py
│   │   ├── lock_store.py
│   │   ├── migrate.py
│   │   ├── nlg
│   │   │   ├── callback.py
│   │   │   ├── generator.py
│   │   │   ├── __init__.py
│   │   │   ├── interpolator.py
│   │   │   └── response.py
│   │   ├── policies
│   │   │   ├── ensemble.py
│   │   │   ├── __init__.py
│   │   │   ├── memoization.py
│   │   │   ├── policy.py
│   │   │   ├── rule_policy.py
│   │   │   ├── ted_policy.py
│   │   │   └── unexpected_intent_policy.py
│   │   ├── processor.py
│   │   ├── run.py
│   │   ├── test.py
│   │   ├── tracker_store.py
│   │   ├── training
│   │   │   ├── converters
│   │   │   │   ├── __init__.py
│   │   │   │   └── responses_prefix_converter.py
│   │   │   ├── __init__.py
│   │   │   ├── interactive.py
│   │   │   ├── story_conflict.py
│   │   │   └── training.py
│   │   ├── train.py
│   │   ├── utils.py
│   │   └── visualize.py
│   ├── engine
│   │   ├── caching.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── graph.py
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   ├── recipes
│   │   │   ├── config_files
│   │   │   │   └── default_config.yml
│   │   │   ├── default_components.py
│   │   │   ├── default_recipe.py
│   │   │   ├── graph_recipe.py
│   │   │   ├── __init__.py
│   │   │   └── recipe.py
│   │   ├── runner
│   │   │   ├── dask.py
│   │   │   ├── __init__.py
│   │   │   └── interface.py
│   │   ├── storage
│   │   │   ├── __init__.py
│   │   │   ├── local_model_storage.py
│   │   │   ├── resource.py
│   │   │   └── storage.py
│   │   ├── training
│   │   │   ├── components.py
│   │   │   ├── fingerprinting.py
│   │   │   ├── graph_trainer.py
│   │   │   ├── hooks.py
│   │   │   └── __init__.py
│   │   └── validation.py
│   ├── exceptions.py
│   ├── graph_components
│   │   ├── converters
│   │   │   ├── __init__.py
│   │   │   └── nlu_message_converter.py
│   │   ├── __init__.py
│   │   ├── providers
│   │   │   ├── domain_for_core_training_provider.py
│   │   │   ├── domain_provider.py
│   │   │   ├── forms_provider.py
│   │   │   ├── __init__.py
│   │   │   ├── nlu_training_data_provider.py
│   │   │   ├── responses_provider.py
│   │   │   ├── rule_only_provider.py
│   │   │   ├── story_graph_provider.py
│   │   │   └── training_tracker_provider.py
│   │   └── validators
│   │       ├── default_recipe_validator.py
│   │       ├── finetuning_validator.py
│   │       └── __init__.py
│   ├── __init__.py
│   ├── jupyter.py
│   ├── __main__.py
│   ├── model.py
│   ├── model_testing.py
│   ├── model_training.py
│   ├── nlu
│   │   ├── classifiers
│   │   │   ├── classifier.py
│   │   │   ├── diet_classifier.py
│   │   │   ├── fallback_classifier.py
│   │   │   ├── __init__.py
│   │   │   ├── keyword_intent_classifier.py
│   │   │   ├── logistic_regression_classifier.py
│   │   │   ├── mitie_intent_classifier.py
│   │   │   ├── regex_message_handler.py
│   │   │   └── sklearn_intent_classifier.py
│   │   ├── constants.py
│   │   ├── convert.py
│   │   ├── emulators
│   │   │   ├── dialogflow.py
│   │   │   ├── emulator.py
│   │   │   ├── __init__.py
│   │   │   ├── luis.py
│   │   │   ├── no_emulator.py
│   │   │   └── wit.py
│   │   ├── extractors
│   │   │   ├── crf_entity_extractor.py
│   │   │   ├── duckling_entity_extractor.py
│   │   │   ├── entity_synonyms.py
│   │   │   ├── extractor.py
│   │   │   ├── __init__.py
│   │   │   ├── mitie_entity_extractor.py
│   │   │   ├── regex_entity_extractor.py
│   │   │   └── spacy_entity_extractor.py
│   │   ├── featurizers
│   │   │   ├── dense_featurizer
│   │   │   │   ├── convert_featurizer.py
│   │   │   │   ├── dense_featurizer.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── lm_featurizer.py
│   │   │   │   ├── mitie_featurizer.py
│   │   │   │   └── spacy_featurizer.py
│   │   │   ├── featurizer.py
│   │   │   ├── __init__.py
│   │   │   └── sparse_featurizer
│   │   │       ├── count_vectors_featurizer.py
│   │   │       ├── __init__.py
│   │   │       ├── lexical_syntactic_featurizer.py
│   │   │       ├── regex_featurizer.py
│   │   │       └── sparse_featurizer.py
│   │   ├── __init__.py
│   │   ├── model.py
│   │   ├── persistor.py
│   │   ├── run.py
│   │   ├── selectors
│   │   │   ├── __init__.py
│   │   │   └── response_selector.py
│   │   ├── test.py
│   │   ├── tokenizers
│   │   │   ├── __init__.py
│   │   │   ├── jieba_tokenizer.py
│   │   │   ├── mitie_tokenizer.py
│   │   │   ├── spacy_tokenizer.py
│   │   │   ├── tokenizer.py
│   │   │   └── whitespace_tokenizer.py
│   │   └── utils
│   │       ├── bilou_utils.py
│   │       ├── hugging_face
│   │       │   ├── __init__.py
│   │       │   ├── registry.py
│   │       │   └── transformers_pre_post_processors.py
│   │       ├── __init__.py
│   │       ├── mitie_utils.py
│   │       ├── pattern_utils.py
│   │       └── spacy_utils.py
│   ├── plugin.py
│   ├── server.py
│   ├── shared
│   │   ├── constants.py
│   │   ├── core
│   │   │   ├── constants.py
│   │   │   ├── conversation.py
│   │   │   ├── domain.py
│   │   │   ├── events.py
│   │   │   ├── generator.py
│   │   │   ├── __init__.py
│   │   │   ├── slot_mappings.py
│   │   │   ├── slots.py
│   │   │   ├── trackers.py
│   │   │   └── training_data
│   │   │       ├── __init__.py
│   │   │       ├── loading.py
│   │   │       ├── story_reader
│   │   │       ├── story_writer
│   │   │       ├── structures.py
│   │   │       ├── visualization.html
│   │   │       └── visualization.py
│   │   ├── data.py
│   │   ├── exceptions.py
│   │   ├── importers
│   │   │   ├── importer.py
│   │   │   ├── __init__.py
│   │   │   ├── multi_project.py
│   │   │   ├── rasa.py
│   │   │   └── utils.py
│   │   ├── __init__.py
│   │   ├── nlu
│   │   │   ├── constants.py
│   │   │   ├── __init__.py
│   │   │   ├── interpreter.py
│   │   │   └── training_data
│   │   │       ├── entities_parser.py
│   │   │       ├── features.py
│   │   │       ├── formats
│   │   │       ├── __init__.py
│   │   │       ├── loading.py
│   │   │       ├── lookup_tables_parser.py
│   │   │       ├── message.py
│   │   │       ├── schemas
│   │   │       ├── synonyms_parser.py
│   │   │       ├── training_data.py
│   │   │       └── util.py
│   │   └── utils
│   │       ├── cli.py
│   │       ├── common.py
│   │       ├── __init__.py
│   │       ├── io.py
│   │       ├── pykwalify_extensions.py
│   │       ├── schemas
│   │       │   ├── config.yml
│   │       │   ├── domain.yml
│   │       │   ├── events.py
│   │       │   ├── __init__.py
│   │       │   ├── model_config.yml
│   │       │   └── stories.yml
│   │       └── validation.py
│   ├── telemetry.py
│   ├── utils
│   │   ├── common.py
│   │   ├── converter.py
│   │   ├── endpoints.py
│   │   ├── __init__.py
│   │   ├── io.py
│   │   ├── llm.py
│   │   ├── log_utils.py
│   │   ├── plotting.py
│   │   ├── tensorflow
│   │   │   ├── callback.py
│   │   │   ├── constants.py
│   │   │   ├── crf.py
│   │   │   ├── data_generator.py
│   │   │   ├── environment.py
│   │   │   ├── exceptions.py
│   │   │   ├── __init__.py
│   │   │   ├── layers.py
│   │   │   ├── layers_utils.py
│   │   │   ├── metrics.py
│   │   │   ├── model_data.py
│   │   │   ├── model_data_utils.py
│   │   │   ├── models.py
│   │   │   ├── rasa_layers.py
│   │   │   ├── transformer.py
│   │   │   └── types.py
│   │   └── train_utils.py
│   ├── validator.py
│   └── version.py
├── README.md
├── scripts
│   ├── download_transformer_model.py
│   ├── evaluate_release_tag.py
│   ├── lint_changelog_files.sh
│   ├── lint_python_docstrings.sh
│   ├── ping_slack_about_package_release.sh
│   ├── poetry-version.sh
│   ├── prepare_nightly_release.py
│   ├── publish_gh_release_notes.py
│   ├── push_docs_to_branch.sh
│   ├── read_tensorflow_version.sh
│   ├── release.py
│   └── write_keys_file.sh
├── secrets.tar.enc
├── security.txt
├── stubs
│   ├── aio_pika
│   │   ├── __init__.pyi
│   │   └── robust_channel.pyi
│   ├── sanic.pyi
│   └── socketio.pyi
├── test_environments
│   ├── message_and_event_brokers
│   │   ├── kafka
│   │   │   ├── no_authentication
│   │   │   │   ├── docker-compose.yml
│   │   │   │   └── README.md
│   │   │   ├── README.md
│   │   │   ├── sasl_plain
│   │   │   │   ├── no_tls
│   │   │   │   └── with_tls
│   │   │   └── sasl_scram
│   │   │       ├── no_tls
│   │   │       └── with_tls
│   │   └── README.md
│   └── README.md
├── tests
│   ├── cli
│   │   ├── conftest.py
│   │   ├── __init__.py
│   │   ├── test_cli.py
│   │   ├── test_rasa_data.py
│   │   ├── test_rasa_evaluate_markers.py
│   │   ├── test_rasa_export.py
│   │   ├── test_rasa_init.py
│   │   ├── test_rasa_interactive.py
│   │   ├── test_rasa_run.py
│   │   ├── test_rasa_shell.py
│   │   ├── test_rasa_test.py
│   │   ├── test_rasa_train.py
│   │   ├── test_rasa_visualize.py
│   │   ├── test_rasa_x.py
│   │   └── test_utils.py
│   ├── conftest.py
│   ├── core
│   │   ├── actions
│   │   │   ├── __init__.py
│   │   │   ├── test_forms.py
│   │   │   ├── test_loops.py
│   │   │   └── test_two_stage_fallback.py
│   │   ├── channels
│   │   │   ├── __init__.py
│   │   │   ├── test_botframework.py
│   │   │   ├── test_cmdline.py
│   │   │   ├── test_facebook.py
│   │   │   ├── test_hangouts.py
│   │   │   ├── test_slack.py
│   │   │   ├── test_telegram.py
│   │   │   ├── test_twilio.py
│   │   │   └── test_twilio_voice.py
│   │   ├── conftest.py
│   │   ├── evaluation
│   │   │   ├── __init__.py
│   │   │   ├── test_marker.py
│   │   │   ├── test_marker_stats.py
│   │   │   └── test_marker_tracker_loader.py
│   │   ├── featurizers
│   │   │   ├── __init__.py
│   │   │   ├── test_precomputation.py
│   │   │   ├── test_single_state_featurizers.py
│   │   │   └── test_tracker_featurizer.py
│   │   ├── __init__.py
│   │   ├── nlg
│   │   │   ├── callback.py
│   │   │   ├── __init__.py
│   │   │   └── test_response.py
│   │   ├── policies
│   │   │   ├── __init__.py
│   │   │   ├── test_rule_policy.py
│   │   │   ├── test_ted_policy.py
│   │   │   └── test_unexpected_intent_policy.py
│   │   ├── test_actions.py
│   │   ├── test_agent.py
│   │   ├── test_broker.py
│   │   ├── test_channels.py
│   │   ├── test_ensemble.py
│   │   ├── test_evaluation.py
│   │   ├── test_examples.py
│   │   ├── test_exporter.py
│   │   ├── test_http_interpreter.py
│   │   ├── test_lock_store.py
│   │   ├── test_migrate.py
│   │   ├── test_nlg.py
│   │   ├── test_policies.py
│   │   ├── test_processor.py
│   │   ├── test_restore.py
│   │   ├── test_run.py
│   │   ├── test_test.py
│   │   ├── test_tracker_stores.py
│   │   ├── test_training.py
│   │   ├── test_utils.py
│   │   ├── training
│   │   │   ├── __init__.py
│   │   │   ├── test_interactive.py
│   │   │   └── test_story_conflict.py
│   │   └── utilities.py
│   ├── dialogues.py
│   ├── docs
│   │   ├── __init__.py
│   │   ├── test_docs_embedded_modules.py
│   │   ├── test_docs_header_hierarchy.py
│   │   ├── test_docs_training_data.py
│   │   └── test_docs_use_base_url.py
│   ├── engine
│   │   ├── conftest.py
│   │   ├── graph_components_test_classes.py
│   │   ├── __init__.py
│   │   ├── recipes
│   │   │   ├── __init__.py
│   │   │   ├── test_default_recipe.py
│   │   │   ├── test_graph_recipe.py
│   │   │   └── test_recipe.py
│   │   ├── runner
│   │   │   ├── __init__.py
│   │   │   └── test_dask.py
│   │   ├── storage
│   │   │   ├── __init__.py
│   │   │   ├── test_local_model_storage.py
│   │   │   ├── test_resource.py
│   │   │   └── test_storage.py
│   │   ├── test_caching.py
│   │   ├── test_graph_node.py
│   │   ├── test_graph.py
│   │   ├── test_loader.py
│   │   ├── test_validation.py
│   │   └── training
│   │       ├── __init__.py
│   │       ├── test_components.py
│   │       ├── test_fingerprinting.py
│   │       ├── test_graph_trainer.py
│   │       └── test_hooks.py
│   ├── examples
│   │   └── test_example_bots_training_data.py
│   ├── graph_components
│   │   ├── converters
│   │   │   ├── __init__.py
│   │   │   └── test_nlu_message_converter.py
│   │   ├── __init__.py
│   │   ├── providers
│   │   │   ├── __init__.py
│   │   │   ├── test_domain_for_core_training_provider.py
│   │   │   ├── test_domain_provider.py
│   │   │   ├── test_forms_provider.py
│   │   │   ├── test_nlu_training_data_provider.py
│   │   │   ├── test_responses_provider.py
│   │   │   ├── test_rule_only_provider.py
│   │   │   ├── test_story_graph_provider.py
│   │   │   └── test_training_tracker_provider.py
│   │   └── validators
│   │       ├── __init__.py
│   │       ├── test_default_recipe_validator.py
│   │       └── test_finetuning_validator.py
│   ├── __init__.py
│   ├── integration_tests
│   │   ├── core
│   │   │   ├── actions
│   │   │   │   ├── conftest.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── test_action.py
│   │   │   ├── brokers
│   │   │   │   ├── conftest.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── test_kafka.py
│   │   │   │   └── test_pika.py
│   │   │   ├── conftest.py
│   │   │   ├── __init__.py
│   │   │   ├── test_agent.py
│   │   │   ├── test_cli_response.py
│   │   │   ├── test_lock_store.py
│   │   │   └── test_tracker_store.py
│   │   └── __init__.py
│   ├── nlu
│   │   ├── classifiers
│   │   │   ├── __init__.py
│   │   │   ├── test_diet_classifier.py
│   │   │   ├── test_fallback_classifier.py
│   │   │   ├── test_keyword_classifier.py
│   │   │   ├── test_logistic_regression_classifier.py
│   │   │   ├── test_mitie_intent_classifier.py
│   │   │   ├── test_regex_message_handler.py
│   │   │   └── test_sklearn_classifier.py
│   │   ├── conftest.py
│   │   ├── emulators
│   │   │   ├── __init__.py
│   │   │   ├── test_dialogflow.py
│   │   │   ├── test_luis.py
│   │   │   ├── test_no_emulator.py
│   │   │   └── test_wit.py
│   │   ├── extractors
│   │   │   ├── __init__.py
│   │   │   ├── test_crf_entity_extractor.py
│   │   │   ├── test_duckling_entity_extractor.py
│   │   │   ├── test_entity_synonyms.py
│   │   │   ├── test_extractor.py
│   │   │   ├── test_mitie_entity_extractor.py
│   │   │   ├── test_regex_entity_extractor.py
│   │   │   └── test_spacy_entity_extractors.py
│   │   ├── featurizers
│   │   │   ├── __init__.py
│   │   │   ├── test_convert_featurizer.py
│   │   │   ├── test_count_vectors_featurizer.py
│   │   │   ├── test_featurizer.py
│   │   │   ├── test_lexical_syntactic_featurizer.py
│   │   │   ├── test_lm_featurizer.py
│   │   │   ├── test_mitie_featurizer.py
│   │   │   ├── test_regex_featurizer.py
│   │   │   └── test_spacy_featurizer.py
│   │   ├── __init__.py
│   │   ├── selectors
│   │   │   ├── __init__.py
│   │   │   └── test_selectors.py
│   │   ├── test_evaluation.py
│   │   ├── test_persistor.py
│   │   ├── test_spacy_utils.py
│   │   ├── test_train.py
│   │   ├── test_utils.py
│   │   ├── tokenizers
│   │   │   ├── __init__.py
│   │   │   ├── test_jieba_tokenizer.py
│   │   │   ├── test_mitie_tokenizer.py
│   │   │   ├── test_spacy_tokenizer.py
│   │   │   ├── test_tokenizer.py
│   │   │   └── test_whitespace_tokenizer.py
│   │   ├── utilities.py
│   │   └── utils
│   │       ├── __init__.py
│   │       ├── test_bilou_utils.py
│   │       ├── test_mitie_utils.py
│   │       ├── test_pattern_utils.py
│   │       └── test_spacy_utils.py
│   ├── regressions
│   │   ├── test_action_extract_slots_11333.py
│   │   ├── test_action_two_stage_fallback_11294.py
│   │   └── test_domain_merge_multiple_files_with_custom_session_config_and_no_session_config.py
│   ├── scripts
│   │   ├── __init__.py
│   │   └── test_evaluate_release_tag.py
│   ├── shared
│   │   ├── core
│   │   │   ├── __init__.py
│   │   │   ├── test_constants.py
│   │   │   ├── test_dialogues.py
│   │   │   ├── test_domain.py
│   │   │   ├── test_events.py
│   │   │   ├── test_generator.py
│   │   │   ├── test_slot_mappings.py
│   │   │   ├── test_slots.py
│   │   │   ├── test_trackers.py
│   │   │   └── training_data
│   │   │       ├── __init__.py
│   │   │       ├── story_reader
│   │   │       ├── story_writer
│   │   │       ├── test_graph.py
│   │   │       ├── test_structures.py
│   │   │       └── test_visualization.py
│   │   ├── importers
│   │   │   ├── __init__.py
│   │   │   ├── test_importer.py
│   │   │   ├── test_multi_project.py
│   │   │   └── test_rasa.py
│   │   ├── __init__.py
│   │   ├── nlu
│   │   │   ├── __init__.py
│   │   │   └── training_data
│   │   │       ├── formats
│   │   │       ├── __init__.py
│   │   │       ├── test_entities_parser.py
│   │   │       ├── test_features.py
│   │   │       ├── test_lookup_tables_parser.py
│   │   │       ├── test_message.py
│   │   │       ├── test_synonyms_parser.py
│   │   │       ├── test_training_data.py
│   │   │       └── test_util.py
│   │   ├── test_data.py
│   │   ├── test_shared.py
│   │   └── utils
│   │       ├── __init__.py
│   │       ├── schemas
│   │       │   ├── __init__.py
│   │       │   └── test_events.py
│   │       ├── test_cli.py
│   │       ├── test_common.py
│   │       ├── test_io.py
│   │       └── test_validation.py
│   ├── test_default_project.py
│   ├── test_dependencies.py
│   ├── test_memory_leak.py
│   ├── test_model.py
│   ├── test_model_testing.py
│   ├── test_model_training.py
│   ├── test_plugin.py
│   ├── test_server.py
│   ├── test_telemetry.py
│   ├── test_validator.py
│   ├── train.py
│   ├── utilities.py
│   └── utils
│       ├── __init__.py
│       ├── tensorflow
│       │   ├── conftest.py
│       │   ├── __init__.py
│       │   ├── test_callback.py
│       │   ├── test_crf.py
│       │   ├── test_data_generator.py
│       │   ├── test_layers.py
│       │   ├── test_layers_utils.py
│       │   ├── test_metrics.py
│       │   ├── test_model_data.py
│       │   ├── test_model_data_utils.py
│       │   ├── test_models.py
│       │   ├── test_rasa_layers.py
│       │   ├── test_tf_environment.py
│       │   └── test_transformer.py
│       ├── test_common.py
│       ├── test_endpoints.py
│       ├── test_io.py
│       ├── test_llm.py
│       ├── test_plotting.py
│       └── test_train_utils.py
├── tests_deployment
│   ├── docker-compose.integration.yml
│   ├── docker-compose.kafka.yml
│   ├── kafka_server_jaas.conf
│   └── README.md
├── tree.md
└── trivy-secret.yaml

267 directories, 1244 files
