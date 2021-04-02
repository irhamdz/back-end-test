function improvedJson(param) {
    let result = {}
    let param_len = param.length;

    if (param_len > 0) {
        let obj_values = [];
        let obj_keys = Object.keys(param[0]);
        let i;
        for (i = 0; i < param_len; i++) {
            obj_values.push(Object.values(param[i]));
        }
        result = {"h": obj_keys, "d": obj_values};
    }

    return result;
}