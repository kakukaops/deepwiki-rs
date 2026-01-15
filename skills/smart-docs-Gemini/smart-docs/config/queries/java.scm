; 定义
(class_declaration name: (identifier) @definition.class)
(interface_declaration name: (identifier) @definition.interface)
(method_declaration name: (identifier) @definition.method)

; 继承与实现
(superclass (type_identifier) @reference.extends)
(super_interfaces (type_list (type_identifier) @reference.extends))

; 调用
(method_invocation name: (identifier) @reference.call)
(object_creation_expression type: (type_identifier) @reference.call) ; 构造函数调用

; ... (原有内容) ...
(import_declaration) @reference.import