; 定义
(function_definition name: (identifier) @definition.function)
(class_definition name: (identifier) @definition.class)

; 继承
(class_definition superclasses: (argument_list (identifier) @reference.extends))

; 调用 (包括普通调用和属性调用)
(call function: (identifier) @reference.call)
(call function: (attribute attribute: (identifier) @reference.call))

; ... (原有内容) ...
(import_statement) @reference.import
(import_from_statement) @reference.import